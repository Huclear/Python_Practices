from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

w3.middleware_onion.inject(geth_poa_middleware, layer = 0)

contract = w3.eth.contract(address = contract_address, abi = abi)

def login():
    try:
        public_key = input("Input your public key: ")
        password = input("Input password: ")
        w3.geth.personal.unlock_account(public_key, password)
        print(f"Account has been aithorized {account}")
        return account
    except Exception as ex:
        print(f"Authorization exception {ex}")
        print(ex)
        return None
    

def register():
    password = input("Input password: ")
    account = w3.geth.personal.new_account(password)
    print(f"Account has been created {account}")
    return account


def send_eth(account):
    value = input("INput mount of wei for sending")
    tx_hash = contract.functions.sendEth().transact({
        "from": account,
        "value": value
    }
    )

def get_balance(account):
    balance = contract.functions.getBalance().call({
        "from": account
    })
    print(f"Your current balance is {balance}")

def withdraw(account):
    try:
        to = input("Input address: ")
        value = input("INput mount of wei for sending")
        tx_hash = contract.functions.withdrawll(to,amount).transact({
            "from": account
        })
        print(f"Transaction sucessfully completed: {tx_hash}")
    except Exception as ex:
        print(f"An exception occupied while trying to withdraw balance from account {ex}")

def main():
    account = ""
    while(True):
        if(account == "" or account == None):
            choice = input("Сhoose: \n1 - Authorize\n2 - Register")
            match choice:
                case "1":
                    account = login()
                case "2":
                    account = register()
                case _:
                    print("Incorrect operation")
        else:
            choice = int(input("Select the operation:\n1 - Send ethers\2 - Get current balace \n3 - See another account's current balance\n4 - Withdraw all\n5 - Exit\n"))
            match choice:
                case 1: 
                    send_eth(account)
                case 2: 
                    get_balance(account)               
                case 3: 
                    pass                
                case 4: 
                    withdraw(account)                
                case 5: 
                    account = ""
                case _:
                    print("Incorrect operation")
                
                
if(__name__ == "__main__"):
    main()
    