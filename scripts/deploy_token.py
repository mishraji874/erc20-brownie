from brownie import OurToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.from_wei(1000, "ether")

def main():
    account = get_account()
    ourToken = OurToken.deploy(initial_supply, {"from": account})
    print(ourToken.name())