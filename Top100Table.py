##############################################################################
# Cryptocurrency Top 100 Ranker App
# Author: Joe Schell
# Date: 07/23/2018
##############################################################################

import json
import requests
import datetime
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style

init(convert=True)

# Change currency type here
convert = 'USD'

# Coin Market Cap global API
global_url = 'https://api.coinmarketcap.com/v2/global/?convert=' + convert

request = requests.get(global_url)
results = request.json()
data = results['data']

global_cap = int(data['quotes'][convert]['total_market_cap'])
global_cap_string = '{:,}'.format(global_cap)

while True:

    # Table Menu loop
    print()
    print('***Coin Market Cap Table Menu***')
    print('The global market cap is $' + global_cap_string)
    print()
    print('1 - Top 100 sorted by rank')
    print('2 - Top 100 sorted by 24 hour change')
    print('3 - Top 100 sorted by 24 hour volume')
    print('0 - Exit')
    print()
    choice = input('Please choose an option (0-3): ')

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array&sort='

    if choice == '1':
        ticker_url += 'rank'
    if choice == '2':
        ticker_url += 'percent_change_24h'
    if choice == '3':
        ticker_url += 'volume_24h'
    if choice == '0':
        break

    request = requests.get(ticker_url)
    results = request.json()
    data = results['data']
    now = datetime.datetime.now()

    print()
    print('This is the most current data as of ' + str(now.hour) + ':' +
        str(now.minute) + ':' + str(now.second) + ' on ' + str(now.month) +
        '/' + str(now.day) + '/' + str(now.year) + '.')

    table = PrettyTable(['Rank', 'Name', 'Price', 'Market Cap',
        'Volume', '1h', '24h', '7d'])

    # Grab data from Global API
    for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quotes'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        # Account for None-type
        if hour_change is not None:
            if hour_change > 0:
                hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change is not None:
            if day_change > 0:
                day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change is not None:
            if week_change > 0:
                week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        if volume is not None:
            volume_string = '{:,}'.format(volume)

        if market_cap is not None:
            market_cap_string = '{:,}'.format(market_cap)

        # Add rows to table
        table.add_row([rank, name + ' (' + symbol + ')',
                       '$' + str(price), '$' + str(market_cap),
                       '$' + volume_string, str(hour_change),
                       str(day_change), str(week_change)])

    print()
    print(table)
    print()

    choice = input('Display Table Menu Again? (y/n): ')

    if choice == 'n':
        break
