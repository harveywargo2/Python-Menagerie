import pandas as pd
import gurulegacy.annual
from datetime import date


def to_df(ticker: str, token: str):
    ann_df = gurulegacy.annual.to_df(ticker, token)
    owner_df = pd.DataFrame(index=ann_df.index)
    owner_df['MarketCap'] = ann_df['valuation_and_quality.Market Cap'].astype(float)
    owner_df['Revenue'] = ann_df['income_statement.Revenue'].astype(float)
    owner_df['CFO'] = ann_df['cashflow_statement.Cash Flow from Operations'].astype(float)
    owner_df['FCF'] = ann_df['cashflow_statement.Free Cash Flow'].astype(float)
    owner_df['SharesOutstanding'] = ann_df['income_statement.Shares Outstanding (Diluted Average)'].astype(float)
    owner_df['Issues'] = ann_df['cashflow_statement.Issuance of Stock'].astype(float)
    owner_df['BuyBack'] = ann_df['cashflow_statement.Repurchase of Stock'].astype(float)
    owner_df['Dividends'] = ann_df['cashflow_statement.Cash Flow for Dividends'].astype(float)
    return owner_df


def to_csv(ticker: str, token: str):
    own_df = to_df(ticker, token)
    return own_df.to_csv(ticker.upper() + '-OwnerData@' + str(date.today()) + '.csv')

