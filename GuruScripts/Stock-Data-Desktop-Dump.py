import keys.guruapi
import GuruWrangler.jupyterdata
import GuruWrangler.dyt
import os

token = keys.guruapi.token
ticker = input('Enter Stock Ticker: ').upper()

# Windows
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

os.chdir(desktop)

# GuruWrangler.jupyterdata.to_csv(ticker, token)
# GuruWrangler.dyt.to_csv(ticker, token)

print(GuruWrangler.jupyterdata.to_df(ticker, token))


