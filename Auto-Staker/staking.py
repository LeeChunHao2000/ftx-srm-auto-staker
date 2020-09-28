import sys, logging

from FTX.client import Client

logging.basicConfig(
    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler('log.txt')],
    level=logging.INFO,
	format = '[%(asctime)s %(levelname)-8s] %(message)s',
	datefmt = '%Y%m%d %H:%M:%S',
	)

# SRM Coins
SRMS = ['SRM', 'SRM_LOCKED', 'MSRM', 'MSRM_LOCKED']

def stake(client, coin):
    """
    :param client: the FTX client class 
    :param coin: the staking coin of srm
    :return: a list contains result
    """
    
    balance = client.get_private_wallet_single_balance(coin)

    if balance is None:
        return
    
    free = balance['free']

    if free > 0:
        client.set_private_srm_stake(coin, free)
        logging.info(f"Coin: {coin} Stake: {free}")

def check(client):
    """
    :param client: the FTX client class
    :return: a list contains result
    """

    for coin in SRMS:
        stake(client, coin)