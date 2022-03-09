from brownie import SimpleStor, accounts, config


def read_contract():
    simple_storage = SimpleStor[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
