"""
Currency Converter
"""
import requests, json

xe_rates = {}


def start_exchange():
    user_currency = str(input())
    while True:
        wanted_currency = str(input())

        if wanted_currency == '':
            break

        coins = int(input())
        rates = get_rates(user_currency)

        if user_currency == 'eur':
            xe_rates['usd'] = rates['usd']['rate']
        elif user_currency == 'usd':
            xe_rates['eur'] = rates['eur']['rate']
        else:
            xe_rates['eur'] = rates['eur']['rate']
            xe_rates['usd'] = rates['usd']['rate']

        print('Checking the cache...')

        try:
            xe_rate = xe_rates[wanted_currency]
            print('Oh! It is in the cache!')
        except Exception:
            print('Sorry, but it is not in the cache!')

            xe_rates[wanted_currency] = rates[wanted_currency]['rate']
            xe_rate = xe_rates[wanted_currency]
        print(f'You received {round(coins*xe_rate, 2)} {wanted_currency}.')


def get_rates(currency):
    url = f"http://www.floatrates.com/daily/{currency}.json"
    response = requests.get(url)
    return response.json()


start_exchange()
