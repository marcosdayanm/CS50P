import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

try:
    q = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
dataformat = data.json()

#print(json.dumps(dataformat, indent=2),'\n\n\n')

pricebtc = dataformat['bpi']['USD']['rate_float']
finalprice = q*pricebtc

print(f"${finalprice:,.4f}")



