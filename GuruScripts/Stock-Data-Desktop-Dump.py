import keys.guruapi
import GuruWrangler.annualdata
import GuruWrangler.dailydata
import os

token = keys.guruapi.token
ticker = input('Enter Stock Ticker: ').upper()

# Windows
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

os.chdir(desktop)

GuruWrangler.annualdata.to_csv(ticker, token)
GuruWrangler.dailydata.to_csv(ticker, token)




