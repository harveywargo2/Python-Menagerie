import GuruWrangler.dividend
import GuruWrangler.price
from datetime import date


def to_df(ticker: str, token: str):
    div_df = GuruWrangler.dividend.to_df(ticker, token)
    div_df2 = div_df.loc[div_df["type"] != 'Special Div.']
    div_ex_df = div_df2.drop(['record_date', 'pay_date', 'type', 'currency'], axis=1)

    price_df = GuruWrangler.price.to_df(ticker, token)
    div_frequency = 4

    combined_df = price_df.join(div_ex_df)
    combined_df.rename_axis('Date', axis='columns')
    combined_df.rename(columns={'amount': 'ExDiv'}, inplace=True)
    combined_df['DivPay'] = combined_df['ExDiv']
    div_var = 0

    for index, row in combined_df.iterrows():
        if row['DivPay'] > 0:
            div_var = row['DivPay']
        else:
            row['DivPay'] = div_var

    combined_df['DivPeriod'] = div_frequency
    combined_df['FwdDiv'] = combined_df['DivPay'] * combined_df['DivPeriod']
    combined_df['FwdDivYield'] = combined_df['FwdDiv'] / combined_df['SharePrice']
    combined_df['Price/Div_Fwd'] = combined_df['SharePrice'] / combined_df['FwdDiv']

    current_year = date.today().year

    for date_index, row in combined_df.iterrows():
        if current_year - date_index.year >= 25:
            combined_df.drop(date_index, inplace=True)

    return combined_df


def to_csv(ticker: str, token: str):
    dump = to_df(ticker, token)
    return dump.to_csv(ticker.upper() + '-DytData@' + str(date.today()) + '.csv')

