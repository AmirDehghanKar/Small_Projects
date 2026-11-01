#EN 
#It fetches the live Bitcoin price from the CoinLore API (id 90) and sends it as an SMS through
#Kavenegar to a phone number. A second price (id 80, likely Ethereum) is fetched but never used.

import os

import kavenegar
import requests

API_URL = 'https://api.coinlore.net/api/ticker/'
BITCOIN_ID = 90


def get_bitcoin_price():
    response = requests.get(API_URL, params={'id': BITCOIN_ID}, timeout=10)
    response.raise_for_status()
    return float(response.json()[0]['price_usd'])


def send_sms(message):
    api = kavenegar.KavenegarAPI(os.environ['KAVENEGAR_API_KEY'])
    params = {
        'sender': os.environ.get('KAVENEGAR_SENDER', ''),
        'receptor': os.environ['SMS_RECEIVER'],
        'message': message,
    }
    return api.sms_send(params)


def main():
    try:
        price = get_bitcoin_price()
        result = send_sms(f'قیمت لحظه ای بیت کوین {price:,.0f} دلار است')
        print(result)
    except (requests.RequestException, KeyError, IndexError, ValueError) as e:
        print('Failed to fetch price:', e)
    except kavenegar.APIException as e:
        print('Kavenegar error:', e)
    except kavenegar.HTTPException as e:
        print('Network error:', e)


if __name__ == '__main__':
    main()