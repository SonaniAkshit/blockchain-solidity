import json
import os
from dotenv import load_dotenv
from web3 import Web3
from web3.middleware.proof_of_authority import ExtraDataToPOAMiddleware
from solcx import compile_standard, install_solc

# Load environment variables (if needed)
load_dotenv()

# Read Solidity source code
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Install Solidity compiler
print("Installing Solidity compiler...")
install_solc("0.6.0")

# Compile Solidity contract
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

# Save compiled output
with open("SimpleStorage.json", "w") as file:
    json.dump(compiled_sol, file)

# Extract bytecode and ABI
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = json.loads(compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"])["output"]["abi"]

# --- Setup blockchain connection ---
# Local Ganache (default)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337  # Ganache default

# Inject POA middleware for compatible networks (optional for Ganache)
w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

if not w3.is_connected():
    raise Exception("Web3 is not connected to blockchain!")

print("Connected to blockchain")

# --- Your account details ---
my_address = "0xBbECB965bC0B35F77AB7a64C7356c0A0f45f3Acc"
private_key = "0xbb5cd60fdb75c89b7472c26201c04b6a5af579d89df9a1ebf418215c049d702e"

# --- Deploy the contract ---
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.get_transaction_count(my_address)

transaction = SimpleStorage.constructor().build_transaction({
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce,
    "gasPrice": w3.eth.gas_price,
})

# Sign + send
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

print("Waiting for deployment...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Contract deployed at: {tx_receipt.contractAddress}")

# --- Interact with deployed contract ---
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Read initial value
print(f"Initial Stored Value: {simple_storage.functions.retrieve().call()}")

# Send a transaction to update the value
store_txn = simple_storage.functions.store(15).build_transaction({
    "chainId": chain_id,
    "from": my_address,
    "nonce": nonce + 1,
    "gasPrice": w3.eth.gas_price,
})

signed_store_txn = w3.eth.account.sign_transaction(store_txn, private_key=private_key)
print("Updating stored value...")
tx_store_hash = w3.eth.send_raw_transaction(signed_store_txn.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_store_hash)

# Verify updated value
print(f"Updated Stored Value: {simple_storage.functions.retrieve().call()}")
