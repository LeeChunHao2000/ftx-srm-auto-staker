#!C:\Users\AS\AppData\Local\Programs\Python\Python37-32\python.exe

import sys, time, logging

from staking import check
from FTX.client import Client

logging.basicConfig(
    handlers = [logging.StreamHandler(sys.stdout), logging.FileHandler('log.txt')],
    level = logging.INFO,
	format = '[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt = '%Y%m%d %H:%M:%S',
	)

def checking(client):
    if 'error' in client.get_private_wallet_balances():
        print ('API Setting Error! Please try again!')
        return True
    return False

def setting():
    api_key = str(input('Set up your API Key: '))
    api_secret = str(input('Set up your API Secret: '))
    client = Client(api_key, api_secret)

    # Check API
    while checking(client):
        api_key = str(input('Set up your API Key: '))
        api_secret = str(input('Set up your API Secret: '))
        client = Client(api_key, api_secret)
    logging.info(f"API Set Up Success")
    return client

def main():
    client = setting()
    while True:
        logging.info(f"SRMS Balances Check")
        check(client)
        time.sleep(60 * 60)

if __name__ == "__main__":
    main()