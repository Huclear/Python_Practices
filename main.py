from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

w3.middleware_onion.inject(geth_poa_middleware, layer = 0)

contract = w3.eth.contract(address = contract_address, abi = abi)
print(contract_address)
print(w3.eth.get_balance(Web3.to_checksum_address('0x1512f83aa5893767ae5e1afa3e7d933d08d61fa8')))
print(w3.eth.get_balance(Web3.to_checksum_address('0x3f4317291bce98de738a4e762618478ad771d0df')))
print(w3.eth.get_balance(Web3.to_checksum_address('0x910c694a6e8235b036ed3825ff16bdc4a13673c0')))
print(w3.eth.get_balance(Web3.to_checksum_address('0xc77037c9a9cec6460c188a6ee4bced70013416bc')))
print(w3.eth.get_balance(Web3.to_checksum_address('0xb4eb322548b837747ac928e21ab2a8acd4b2c714')))