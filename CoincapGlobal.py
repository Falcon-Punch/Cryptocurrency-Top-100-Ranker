import json
import requests

globalURL = 'https://api.coinmarketcap.com/v2/global/'

request = requests.get(globalURL)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
