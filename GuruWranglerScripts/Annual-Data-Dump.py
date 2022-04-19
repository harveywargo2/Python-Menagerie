import pandas as pd
import gurufocus.dataframe
import keys.guruapi
from datetime import date
import os


token = keys.guruapi.token
ticker = input('Enter Stock Ticker: ').upper()

# Pull gurufocus data
df_init = gurufocus.dataframe.annuals(ticker, token)

# Assign Dataframes
margin_df = pd.DataFrame(index=df_init.index)
ps_df = pd.DataFrame(index=df_init.index)
grow_df = pd.DataFrame(index=df_init.index)
owner_df = pd.DataFrame(index=df_init.index)
debt_df = pd.DataFrame(index=df_init.index)


# Per Share Dataframe
ps_df['LowPrice'] = df_init['valuation_and_quality.Lowest Stock Price'].astype(float)
ps_df['HighPrice'] = df_init['valuation_and_quality.Highest Stock Price'].astype(float)

ps_df['RPS'] = df_init['per_share_data_array.Revenue per Share'].astype(float)
ps_df['LP/R'] = ps_df['LowPrice'] / ps_df['RPS']
ps_df['HP/R'] = ps_df['HighPrice'] / ps_df['RPS']

ps_df['FCFPS'] = df_init['per_share_data_array.Free Cash Flow per Share'].astype(float)
ps_df['LP/FCF'] = ps_df['LowPrice'] / ps_df['FCFPS']
ps_df['HP/FCF'] = ps_df['HighPrice'] / ps_df['FCFPS']

ps_df['EPS'] = df_init['per_share_data_array.Earnings per Share (Diluted)'].astype(float)
ps_df['LP/E'] = ps_df['LowPrice'] / ps_df['EPS']
ps_df['HP/E'] = ps_df['HighPrice'] / ps_df['EPS']

ps_df = ps_df.drop(index=['TTM'])


# Margins
margin_df['Revenue'] = df_init['income_statement.Revenue'].astype(float)

margin_df['COGS'] = df_init['income_statement.Cost of Goods Sold'].astype(float)
margin_df['GrossProfit'] = df_init['income_statement.Gross Profit'].astype(float)
margin_df['GPM'] = margin_df['GrossProfit'] / margin_df['Revenue']

margin_df['OperatingProfit'] = df_init['income_statement.Operating Income'].astype(float)
margin_df['OPEX'] = df_init['income_statement.Total Operating Expense'].astype(float)
margin_df['OPM'] = margin_df['OperatingProfitProfit'] / margin_df['Revenue']

margin_df['NetProfit'] = df_init['income_statement.Net Income'].astype(float)
margin_df['NetMargin'] = margin_df['NetProfit'] / margin_df['Revenue']

margin_df['CashFromOps'] = df_init['cashflow_statement.Cash Flow from Operations'].astype(float)
margin_df['CfoMargin'] = margin_df['CashFromOps'] / margin_df['Revenue']

margin_df['CAPEX'] = df_init['cashflow_statement.Capital Expenditure'].astype(float)
margin_df['CapexMargin'] = margin_df['CashFromOps'] / margin_df['Revenue']

margin_df['FCF'] = df_init['cashflow_statement.Free Cash Flow'].astype(float)
margin_df['FcfMargin'] = margin_df['FCF'] / margin_df['Revenue']

margin_df['Dividends'] = df_init['cashflow_statement.Cash Flow for Dividends'].astype(float)
margin_df['Dividends'] = margin_df['Dividends'] / margin_df['Revenue']

margin_df = margin_df.drop(index=['TTM'])


# Growth
grow_df['Revenue'] = margin_df['Revenue'].astype(float)
grow_df['RevGro'] = ""

grow_df['Dividend'] = df_init['cashflow_statement.Cash Flow for Dividends'].astype(float)
grow_df['DivGro'] = ""

grow_df['DivPerShare'] = df_init['per_share_data_array.Dividends per Share'].astype(float)
grow_df['DPSGro'] = ""

grow_df['MarketValue'] = df_init['valuation_and_quality.Market Cap'].astype(float)
grow_df['MVGro'] = ""

grow_df['SharesOutstanding'] = df_init['income_statement.Shares Outstanding (Diluted Average)'].astype(float)
grow_df['ShareGro'] = ""

grow_df = grow_df.drop(index=['TTM'])


# Ownership
owner_df['Issues'] = df_init['cashflow_statement.Issuance of Stock'].astype(float)
owner_df['BuyBack'] = df_init['cashflow_statement.Repurchase of Stock'].astype(float)
owner_df['Dividend'] = df_init['cashflow_statement.Cash Flow for Dividends'].astype(float)
owner_df['OwnersDistribution'] = ""


# Balance Sheet
debt_df['CashFromOps'] = df_init['cashflow_statement.Cash Flow from Operations'].astype(float)
debt_df['FCF'] = df_init['cashflow_statement.Free Cash Flow'].astype(float)

debt_df['CashAndEquivalents'] = df_init['balance_sheet.Cash and Cash Equivalents'].astype(float)
debt_df['MarketSecurities'] = df_init['balance_sheet.Marketable Securities'].astype(float)

debt_df['Treasury'] = df_init['balance_sheet.Treasury Stock'].astype(float)

debt_df['CurrentAssets'] = df_init['balance_sheet.Total Current Assets'].astype(float)
debt_df['LongAssets'] = df_init['balance_sheet.Total Long-Term Assets'].astype(float)

debt_df['CurrentLiabilities'] = df_init['balance_sheet.Total Current Liabilities'].astype(float)
debt_df['LongLiabilities'] = df_init['balance_sheet.Total Long-Term Liabilities'].astype(float)

debt_df = debt_df.drop(index=['TTM'])


# Windows
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)

ps_df.to_csv(ticker.upper() + '-PerShare@' + str(date.today()) + '.csv')
margin_df.to_csv(ticker.upper() + '-Margin@' + str(date.today()) + '.csv')
grow_df.to_csv(ticker.upper() + '-Growth@' + str(date.today()) + '.csv')
owner_df.to_csv(ticker.upper() + '-Owner@' + str(date.today()) + '.csv')
debt_df.to_csv(ticker.upper() + '-Debt@' + str(date.today()) + '.csv')



