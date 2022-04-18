import pandas as pd
import GuruWrangler.annual
from datetime import date


def to_df(ticker: str, token: str):
    df = GuruWrangler.annual.to_df(ticker, token)
    data_df = pd.DataFrame(index=df.index)
    data_df['Price_Low'] = df['valuation_and_quality.Lowest Stock Price'].astype(float)
    data_df['Price_High'] = df['valuation_and_quality.Highest Stock Price'].astype(float)
    data_df['RPS'] = df['per_share_data_array.Revenue per Share'].astype(float)
    data_df['FCFS'] = df['per_share_data_array.Free Cash Flow per Share'].astype(float)
    data_df['EPS'] = df['per_share_data_array.Earnings per Share (Diluted)'].astype(float)
    data_df['DPS'] = df['per_share_data_array.Dividends per Share'].astype(float)
    data_df['Revenue'] = df['income_statement.Revenue'].astype(float)
    data_df['COGS'] = df['income_statement.Cost of Goods Sold'].astype(float)
    data_df['GrossProfit'] = df['income_statement.Gross Profit'].astype(float)
    data_df['OperatingProfit'] = df['income_statement.Operating Income'].astype(float)
    data_df['OPEX'] = df['income_statement.Total Operating Expense'].astype(float)
    data_df['NetProfit'] = df['income_statement.Net Income'].astype(float)
    data_df['CashFromOps'] = df['cashflow_statement.Cash Flow from Operations'].astype(float)
    data_df['CAPEX'] = df['cashflow_statement.Capital Expenditure'].astype(float)
    data_df['FreeCashFlow'] = df['cashflow_statement.Free Cash Flow'].astype(float)
    data_df['SharesOutstanding'] = df['income_statement.Shares Outstanding (Diluted Average)'].astype(float)
    data_df['Issues'] = df['cashflow_statement.Issuance of Stock'].astype(float)
    data_df['BuyBack'] = df['cashflow_statement.Repurchase of Stock'].astype(float)
    data_df['Dividends'] = df['cashflow_statement.Cash Flow for Dividends'].astype(float)
    data_df['CashAndEquivalents'] = df['balance_sheet.Cash and Cash Equivalents'].astype(float)
    data_df['MarketSecurities'] = df['balance_sheet.Marketable Securities'].astype(float)
    data_df['Treasury'] = df['balance_sheet.Treasury Stock'].astype(float)
    data_df['CurrentAssets'] = df['balance_sheet.Total Current Assets'].astype(float)
    data_df['LongAssets'] = df['balance_sheet.Total Long-Term Assets'].astype(float)
    data_df['CurrentLiabilities'] = df['balance_sheet.Total Current Liabilities'].astype(float)
    data_df['LongLiabilities'] = df['balance_sheet.Total Long-Term Liabilities'].astype(float)
    data_df = data_df.drop(index=['TTM'])
    return data_df


def to_csv(ticker: str, token: str):
    data_df = to_df(ticker, token)
    return data_df.to_csv(ticker.upper() + '-ad.csv')