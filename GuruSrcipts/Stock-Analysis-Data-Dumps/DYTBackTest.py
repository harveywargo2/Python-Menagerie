import pandas as pd
import gurufocus.dataframe
import keys.guruapi
from datetime import date
import os


token = keys.guruapi.token
ticker = input('Enter Stock Ticker: ').upper()
median = float(input("Enter Median: ")) / 100
mos = float(input("Enter MOS: ")) / 100
dmos = float(input("Enter DMOS: ")) / 100


# Get Data from Gurfocus
annuals = gurufocus.dataframe.annuals(ticker, token)
dividend = gurufocus.dataframe.dividend(ticker, token)
price = gurufocus.dataframe.price(ticker, token)


# Initialize variables & dataframes
div_df1 = dividend
price_df = price
div_frequency = 4
div_var = 0
current_year = date.today().year


# Trim out special dividends
div_df2 = div_df1.loc[div_df1["type"] != 'Special Div.']


# Drop unused columns
div_ex_df = div_df2.drop(['record_date', 'pay_date', 'type', 'currency'], axis=1)

combined_df = price_df.join(div_ex_df)
combined_df.rename_axis('Date', axis='columns')
combined_df.rename(columns={'amount': 'ExDiv'}, inplace=True)
combined_df['DivPay'] = combined_df['ExDiv']


# Trim data set to 30 years
for date_index, row in combined_df.iterrows():
    if current_year - date_index.year >= 30:
        combined_df.drop(date_index, inplace=True)


# Calc fwd dividend from combined dataframe
for index, row in combined_df.iterrows():
    if row['DivPay'] > 0:
        div_var = row['DivPay']
    else:
        row['DivPay'] = div_var

combined_df['DivPeriod'] = div_frequency
combined_df['FwdDiv'] = combined_df['DivPay'] * combined_df['DivPeriod']
combined_df['FwdDivYield'] = combined_df['FwdDiv'] / combined_df['SharePrice']


# Back Test Columns
combined_df['Median'] = median
combined_df['MOS'] = mos
combined_df['DMOS'] = dmos


combined_df.loc[combined_df['FwdDivYield'] >= median, 'MedianBackTest'] = 'FairBuy'
combined_df.loc[combined_df['FwdDivYield'] >= mos, 'MOSBackTest'] = 'GoodBuy'
combined_df.loc[combined_df['FwdDivYield'] >= dmos, 'DMOSBackTest'] = 'GreatBuy'


# Windows
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)

combined_df.to_csv(ticker.upper() + '-DYTBT@' + str(date.today()) + '.csv')

