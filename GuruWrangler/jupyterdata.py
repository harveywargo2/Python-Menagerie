import pandas as pd
import GuruWrangler.annual
from datetime import date


def to_df(token: str, ticker: str):
    ann_df = GuruWrangler.annual.to_df(token, ticker)
    data_df = pd.DataFrame(index=ann_df.index)

    data_df['Price_Low'] = ann_df['valuation_and_quality.Lowest Stock Price'].astype(float)
    data_df['Price_High'] = ann_df['valuation_and_quality.Highest Stock Price'].astype(float)
    data_df['RPS'] = ann_df['per_share_data_array.Revenue per Share'].astype(float)
    data_df['FCFS'] = ann_df['per_share_data_array.Free Cash Flow per Share'].astype(float)
    data_df['EPS'] = ann_df['per_share_data_array.Earnings per Share (Diluted)'].astype(float)
    data_df['DPS'] = ann_df['per_share_data_array.Dividends per Share'].astype(float)
    data_df['Revenue'] = ann_df['income_statement.Revenue'].astype(float)
    data_df['COGS'] = ann_df['income_statement.Cost of Goods Sold'].astype(float)
    data_df['GrossProfit'] = ann_df['income_statement.Gross Profit'].astype(float)
    data_df['OperatingProfit'] = ann_df['income_statement.Operating Income'].astype(float)
    data_df['OPEX'] = ann_df['income_statement.Total Operating Expense'].astype(float)
    data_df['NetProfit'] = ann_df['income_statement.Net Income'].astype(float)
    data_df['CashFromOps'] = ann_df['cashflow_statement.Cash Flow from Operations'].astype(float)
    data_df['CAPEX'] = ann_df['cashflow_statement.Capital Expenditure'].astype(float)
    data_df['FreeCashFlow'] = ann_df['cashflow_statement.Free Cash Flow'].astype(float)
    data_df['SharesOutstanding'] = ann_df['income_statement.Shares Outstanding (Diluted Average)'].astype(float)
    data_df['Issues'] = ann_df['cashflow_statement.Issuance of Stock'].astype(float)
    data_df['BuyBack'] = ann_df['cashflow_statement.Repurchase of Stock'].astype(float)
    data_df['Dividends'] = ann_df['cashflow_statement.Cash Flow for Dividends'].astype(float)
    data_df['CashAndEquivalents'] = ann_df['balance_sheet.Cash And Cash Equivalents'].astype(float)
    data_df['MarketSecurities'] = ann_df['balance_sheet.Marketable Securities'].astype(float)
    data_df['Treasury'] = ann_df['balance_sheet.Treasury Stock'].astype(float)
    data_df['CurrentAssets'] = ann_df['balance_sheet.Total Current Assets'].astype(float)
    data_df['LongAssets'] = ann_df['balance_sheet.Total Long-Term Assets'].astype(float)
    data_df['CurrentLiabilities'] = ann_df['balance_sheet.Total Current Liabilities'].astype(float)
    data_df['LongLiabilities'] = ann_df['balance_sheet.Total Long-Term Liabilities'].astype(float)

    return data_df
