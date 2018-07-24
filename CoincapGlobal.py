import json
import requests

globalURL = 'https://api.coinmarketcap.com/v2/global/'

request = requests.get(globalURL)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = results['data']['quotes']['USD']['total_market_cap']
global_volume = results['data']['quotes']['USD']['total_volume_24h']

print()
print('There are currently ' + str(active_currencies) + ' active cryptocurrencies.')
