import pandas as pd
import gurulegacy.annual
from datetime import date


def to_df(ticker: str, token: str):
    ann_df = gurulegacy.annual.to_df(ticker, token)
    debt_df = pd.DataFrame(index=ann_df.index)
    debt_df['Revenue'] = ann_df['income_statement.Revenue'].astype(float)
    debt_df['FreeCashFlow'] = ann_df['cashflow_statement.Free Cash Flow'].astype(float)
    debt_df['CashFromOps'] = ann_df['cashflow_statement.Cash Flow from Operations'].astype(float)
    debt_df['CashAndEquivalents'] = ann_df['balance_sheet.Cash And Cash Equivalents'].astype(float)
    debt_df['MarketSecurities'] = ann_df['balance_sheet.Marketable Securities'].astype(float)
    debt_df['Treasury'] = ann_df['balance_sheet.Treasury Stock'].astype(float)
    debt_df['CurrentAssets'] = ann_df['balance_sheet.Total Current Assets'].astype(float)
    debt_df['LongAssets'] = ann_df['balance_sheet.Total Long-Term Assets'].astype(float)
    debt_df['CurrentLiabilities'] = ann_df['balance_sheet.Total Current Liabilities'].astype(float)
    debt_df['LongLiabilities'] = ann_df['balance_sheet.Total Long-Term Liabilities'].astype(float)
    return debt_df


def to_csv(ticker: str, token: str):
    debt_df = to_df(ticker, token)
    return debt_df.to_csv(ticker.upper() + '-DebtData@' + str(date.today()) + '.csv')


