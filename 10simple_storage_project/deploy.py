import json
from solcx import compile_standard, install_solc
from web3 import Web3

# Step 1: Install Solidity Compiler
install_solc("0.8.0")

# Step 2: Read contract
with open("SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Step 3: Compile contract
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# Get bytecode and ABI
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Step 4: Connect to Ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
w3.eth.default_account = w3.eth.accounts[0]  # use first Ganache account

# Step 5: Deploy contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = SimpleStorage.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Contract deployed at:", tx_receipt.contractAddress)

# Step 6: Interact with contract
contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Call (read function)
print("Initial value:", contract.functions.getValue().call())

# Transact (write function)
tx_hash = contract.functions.setValue(55).transact()
w3.eth.wait_for_transaction_receipt(tx_hash)

# Call again
print("Updated value:", contract.functions.getValue().call())
