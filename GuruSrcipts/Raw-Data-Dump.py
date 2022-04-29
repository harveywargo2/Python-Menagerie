import keys.guruapi
import os
import gurufocus.dataframe
from datetime import date


token = keys.guruapi.token
ticker = input('Enter Stock Ticker: ').upper()

# Windows
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

os.chdir(desktop)

annuals = gurufocus.dataframe.annuals(ticker, token)
dividend = gurufocus.dataframe.dividend(ticker, token)
price = gurufocus.dataframe.price(ticker, token)


annuals.to_csv(ticker.upper() + '-Annual@' + str(date.today()) + '.csv')
dividend.to_csv(ticker.upper() + '-Dividend@' + str(date.today()) + '.csv')
price.to_csv(ticker.upper() + '-Price@' + str(date.today()) + '.csv')
