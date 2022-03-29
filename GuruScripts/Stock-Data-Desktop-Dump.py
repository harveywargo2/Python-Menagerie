import keys.guruapi
import GuruWrangler.dividend
import pandas as pd
import os

token = keys.guruapi.token
ticker = input('Enter Stock Ticker: ').upper()

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

print(desktop)


