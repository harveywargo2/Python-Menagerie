import pandas as pd


df = pd.read_csv('MSFT-DailyData@2022-04-18.csv')

df['Date'] = pd.to_datetime(df['Date'])
print(df)

x = df.groupby(df['Date'].dt.year).agg({'SharePrice': ['max', 'min', 'mean', 'median'], 'FwdDivYield': ['max', 'min', 'median', 'mean']})

x.to_csv('test.csv')