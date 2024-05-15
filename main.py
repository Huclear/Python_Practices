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
    

def lettersInSubstr(subStr, letters):
    index = -1
    for ch in subStr:
        if(letters.find(ch) !=null):
            return True
    return False

def register():
    password = input("Input password: ")
    while not(lettersInSubstr(password, 'QWWERTYUIOPASDFGHJKLZXCVBNM')) or not(lettersInSubstr(password, 'qwertyuiopasdfghjklzxcvbnm'))or not(lettersInSubstr(password, '1234567890')) or not(lettersInSubstr(password, '!@#$%^&*()_\\|/,~:;\'\"№')):
        password = input("Password should contain at least 1 capital letter, 1 lowercase letter, 1 special symbol and 1 number\n Re-input your password: ")
    account = w3.geth.personal.new_account(password)
    print(f"Account has been created {account}")
    return account


def send_eth(account):
    value = input("INput mount of wei for sending")
    tx_hash = contract.functions.addToBalance().transact({
        "from": account,
        "value": value
    })
    print(f"Transaction has been sent: {tx_hash.hex()}")

def get_balance(account):
    balance = contract.functions.getBalance().call({
        "from": account
    })
    print(f"Your current balance is {balance}")
def getEstates(account):
    estates = contract.functions.getEstate().call({
        "from": account
    })
    print(f"Tour estates are: \n{estates}")
    
def getAds(account):
    adds = contract.functions.getAds().call()
    print(f"Here are all advertisements: \n{adds}")
    
def createEstate(account, size, addressEstate, estateType):
    if(size < 0 or estateType < 0):
        print("Incorrect size or estateType")
        return
    try:
        tx_hash = contract.functions.createEState(size, addressEstate, estateType).call({
          "from": account
        })
        print(f"Estate was successfully created : {tx_hash}!!!")
    except Exception as ex:
        print(f"Cannot create an estate: {ex}")
        
def createAd(account, idEstate, price):
    if(price < 0 or idEstate < 0):
        print("Incorrect format of price or id")
        return
    try:
        tx_hash = contract.functions.createAd(idEstate, price).call({
            "from": account
        })
        print("Advertisement was successfuly created")
    except Exception as ex:
        print(f"Cannot create an advertisement: {ex}")
def changeEstateStatus(account, idEstate, isActive):
    if(idEstate < 0):
        print("Incorrect format of price id")
        return
    try:
        tx_hash = contract.functions.changeEstateStatus(idEstate, isActive).call({
            "from": account
        })
        print(f"Estate type was successfully changed: {tx_hash}")
    except Exception as ex:
        print(f"Cannot change estate type: {ex}")
    
def changeAdStatus(account, idAd, newStatus):
    if(idAd < 0 or newStatus < 0):
        print("Incorrect format of price id or advertisement status")
        return
    try:
        tx_hash = contract.functions.changeAdStatus(idAd,newStatus).call({
            "from": account,
        })
        print(f"Advertisement type was successfully changed: {tx_hash}")
    except Exception as ex:
        print(f"Cannot change advertisement type: {ex}")
        
def buyEstate(account, idEstate):
    if(idEstate < 0):
        print("Incorrect format of price id")
        return
    try:
        tx_hash = contract.functions.buyEstate(idEstate).call({
            "from": account,
        })
        print(f"Estate was successfully bought: {tx_hash}")
    except Exception as ex:
        print(f"Cannot buy estate: {ex}")

def checkIsActive(idEstate):
    if(idEstate < 0):
        print("Incorrect format of id")
        return
    try:
        isActive = contract.functions.isEstAct(idEstate).call()
        print(f"\nEstate status: {isActive}")
    except Exception as ex:
        print(f"Cannot check estate status: {ex}")

def withdraw(account):
    try:
        amount = input("Input mount of wei for sending")
        if(amount < 0):
            print("Got you, little criminal scum. You cannot withdraw negative amount of money")
            return
        tx_hash = contract.functions.withDraw(amount).call({
            "from": account
        })
        print(f"Successfuly withdrawed: {tx_hash}")
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
            choice = int(input("Select the operation:\n1 - Send ethers\2 - Get current balace \n3 - See another account's current balance\n4 - Withdraw all\n5 - Create new Estate\n6 - Create new advertisement\n7 - Change estate status\n8 - Change advertisement status\n9 - Buy estate\n10 - Get Estates\n11 - Get Advertisements\n12 - Check if Estate is Active\n13 - Exit\tOperation: "))
            match choice:
                case 1: 
                    send_eth(account)
                case 2: 
                    get_balance(account)               
                case 3: 
                    print(f"Account's balance {w3.eth.get_balance(account)}")
                    pass                
                case 4: 
                    withdraw(account)          
                    pass 
                case 5:
                    try:
                        size = int(input("\nInput estate size: "))
                        address = input("\nInput Estate address: ")
                        estateType = int("Select type:\n\t1 - House\n\t2 - Flat\n\t3 - Loft\nEstate type: ")
                        createEstate(account, size, address, estateType)
                    except Exception as ex:
                        print(f"Incorrect input values or {ex}")
                    finally:
                        pass     
                case 6:
                    try:
                        price = int(input("\nInput advertisement price: "))
                        idEstate = int(input("\nInput estate id: "))
                        createAd(account, idEstate, price)
                    except Exception as ex:
                        print(f"Incorrect input values or {ex}")
                    finally:
                        pass     
                case 7:
                    try:
                        estateType = int(input("Select estate type: 0 - Active, 1 - Closed")) == 0
                        idEstate = int(input("Input estate id: "))
                        changeEstateStatus(account, idEstate, estateType)
                    except Exception as ex:
                        print(f"Incorrect input values or {ex}")
                    finally:
                        pass
                case 8:
                    try:
                        adStatus = int(input("Select advertisement type: 0 - Opened, 1 - Closed"))
                        idAd = int(input("Input advertisement id: "))
                        changeAdStatus(account, idAd, adStatus)
                    except Exception as ex:
                        print(f"Incorrect input values or {ex}")
                    finally:
                        pass
                case 9:
                    try:
                        idAd = int(input("Input advertisement id: "))
                        buyEstate(account, idAd)
                    except Exception as ex:
                        print(f"Incorrect input values or {ex}")
                    finally:
                        pass   
                case 10:
                    getEstates()
                    pass     
                case 11:
                    getAds(account)
                    pass
                case 12:
                    try:
                        idEstate = int(input("Input estate id: "))
                        checkIsActive(idEstate)
                    except Exception as ex:
                        print(f"Incorrect input values or {ex}")
                    finally:
                        pass   
                case 13: 
                    account = ""
                    pass
                case _:
                    print("Incorrect operation")
                    pass
                
                
                
if(__name__ == "__main__"):
    main()
    