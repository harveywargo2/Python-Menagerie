import pandas as pd
import GuruWrangler.annual
from datetime import date


def to_df(ticker: str, token: str):
    ann_df = GuruWrangler.annual.to_df(ticker, token)
    margin_df = pd.DataFrame(index=ann_df.index)
    margin_df['Revenue'] = ann_df['income_statement.Revenue'].astype(float)
    margin_df['COGS'] = ann_df['income_statement.Cost of Goods Sold'].astype(float)
    margin_df['GrossProfit'] = ann_df['income_statement.Gross Profit'].astype(float)
    margin_df['OperatingProfit'] = ann_df['income_statement.Operating Income'].astype(float)
    margin_df['OPEX'] = ann_df['income_statement.Total Operating Expense'].astype(float)
    margin_df['NetProfit'] = ann_df['income_statement.Net Income'].astype(float)
    margin_df['CashFromOperations'] = ann_df['cashflow_statement.Cash Flow from Operations'].astype(float)
    margin_df['CFOM'] = margin_df['CashFromOperations'] / margin_df['Revenue']
    margin_df['CAPEX'] = ann_df['cashflow_statement.Capital Expenditure'].astype(float)
    margin_df['CapexMargin'] = margin_df['CAPEX'] / margin_df['Revenue']
    margin_df['FCFM'] = margin_df['FreeCashFlow'] / margin_df['Revenue']
    margin_df['FreeCashFlow'] = ann_df['cashflow_statement.Free Cash Flow'].astype(float)
    return margin_df


def to_csv(ticker: str, token: str):
    margin_df = to_df(ticker, token)
    return margin_df.to_csv(ticker.upper() + '-MarginsData@' + str(date.today()) + '.csv')