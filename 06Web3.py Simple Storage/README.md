# 🧠 Web3.py Simple Storage — Developer Setup Guide

This guide walks you through setting up your local development environment for Ethereum smart contracts using **VS Code**, **Python**, **Web3.py**, **MetaMask**, and **Node.js**.
You’ll be ready to write, deploy, and interact with a simple Solidity smart contract.

---

## ⚙️ 1. Developer Bootcamp Setup Overview

### You’ll install:

* **MetaMask** – for managing Ethereum accounts and test networks
* **Visual Studio Code (VSCode)** – your main coding editor
* **Python 3** – for running Web3.py scripts
* **Node.js** – required for blockchain tools and npm packages
* **Web3.py** – Python library for interacting with Ethereum

---

## 🦊 2. MetaMask Setup

1. Install the MetaMask extension from [https://metamask.io](https://metamask.io)
2. Create a new wallet or import an existing one.
3. Switch to a **Test Network** like **Sepolia** or **Goerli**.
4. Get some free test ETH from a **faucet** (e.g. [https://faucets.chain.link](https://faucets.chain.link)).
5. Keep your **private key** safe and **never share it**.

---

## 💻 3. Installing VS Code

### Download and Install

Go to [https://code.visualstudio.com](https://code.visualstudio.com)
Select your OS (Windows / macOS / Linux) and install VSCode.

### Launch VS Code

* Open it from the Start Menu or Applications folder.
* Familiarize yourself with the UI: **Explorer**, **Terminal**, and **Extensions**.

---

## 🧩 4. Recommended VSCode Extensions

Install these extensions from the VSCode marketplace:

| Extension               | Purpose                                      |
| ----------------------- | -------------------------------------------- |
| Solidity by Juan Blanco | Syntax highlighting and linting for Solidity |
| Prettier                | Auto-formatting your Solidity and JS code    |
| Python                  | Support for Python linting and debugging     |
| Code Spell Checker      | Optional but helpful                         |
| GitLens                 | Version control insights                     |

---

## ⌨️ 5. VSCode Shortcuts

### Common Shortcuts (Windows/Linux)

| Action               | Shortcut           |
| -------------------- | ------------------ |
| Open Terminal        | `Ctrl + ~`         |
| Save File            | `Ctrl + S`         |
| Format Document      | `Shift + Alt + F`  |
| Open Command Palette | `Ctrl + Shift + P` |
| Comment Line         | `Ctrl + /`         |

### macOS Shortcuts

| Action               | Shortcut             |
| -------------------- | -------------------- |
| Open Terminal        | `Control + ~`        |
| Save File            | `Cmd + S`            |
| Format Document      | `Shift + Option + F` |
| Open Command Palette | `Cmd + Shift + P`    |
| Comment Line         | `Cmd + /`            |

---

## 🐍 6. Installing Python

### Step 1: Download

Visit [https://python.org/downloads](https://python.org/downloads) and download the latest version (3.10+).

### Step 2: Add to PATH (Windows)

During installation, **check the box** that says “Add Python to PATH.”

### Step 3: Verify Installation

Open your terminal and run:

```bash
python --version
```

If you see something like `Python 3.11.6`, it’s working.

### Step 4: Install Pip (if missing)

```bash
python -m ensurepip --upgrade
```

### Troubleshooting

If Python isn’t recognized:

* Restart VSCode or your terminal.
* Reinstall Python and ensure “Add to PATH” is selected.

---

## 💾 7. Making and Opening a Folder in VSCode

1. Create a folder for your project:

   ```bash
   mkdir web3py-simple-storage
   cd web3py-simple-storage
   ```
2. Open the folder in VSCode:

   ```bash
   code .
   ```
3. Inside VSCode, create a new file named `SimpleStorage.sol`.

---

## 🌐 8. Setting Up Solidity in VSCode

1. Install the **Solidity** extension by Juan Blanco.

2. Set the **Solidity compiler version**:

   * Open Command Palette → `Ctrl + Shift + P`
   * Type: `Solidity: Select Compiler Version`
   * Choose `v0.8.x`

3. Enable **Formatting on Save**:

   * Go to **File → Preferences → Settings**
   * Search “Format on Save” and check the box.

4. Install **Prettier** for clean formatting.

---

## 🧮 9. Simple Solidity Contract Example

Create a file `SimpleStorage.sol`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public favoriteNumber;

    function store(uint256 _number) public {
        favoriteNumber = _number;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }
}
```

Save the file (`Ctrl + S`).

---

## 🧠 10. Setting Up Python + Web3.py

### Step 1: Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### Step 2: Install Web3.py

```bash
pip install web3
```

### Step 3: Create a Python Script

Make a new file: `deploy.py`

```python
from web3 import Web3
import json

# Connect to local blockchain or testnet
w3 = Web3(Web3.HTTPProvider("https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Load compiled contract ABI and bytecode
with open("SimpleStorage.json") as f:
    contract_json = json.load(f)
    abi = contract_json["abi"]
    bytecode = contract_json["bytecode"]

# Set up your account
private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)
address = account.address

# Deploy contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.get_transaction_count(address)

transaction = SimpleStorage.constructor().build_transaction({
    "from": address,
    "nonce": nonce,
    "gas": 2000000,
    "gasPrice": w3.to_wei("30", "gwei")
})

signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("Deploying contract...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Contract deployed at:", tx_receipt.contractAddress)
```

*(You’ll need to compile the contract in Remix and export ABI + Bytecode as JSON.)*

---

## 🧩 11. Linting and Formatting in VSCode

* **Python** → Use **Black** formatter

  ```bash
  pip install black
  ```

  Format code:

  ```bash
  black your_script.py
  ```

* **Solidity** → Use **Prettier** or built-in formatting from the Solidity plugin
  Save your file and VSCode will auto-format if “Format on Save” is enabled.

---

## 🧭 12. Terminal Basics

| Command            | Description                   |
| ------------------ | ----------------------------- |
| `pwd`              | Show current directory        |
| `ls`               | List files                    |
| `cd foldername`    | Enter folder                  |
| `mkdir foldername` | Create folder                 |
| `code .`           | Open current folder in VSCode |
| `python file.py`   | Run a Python script           |

---

## 🧱 13. Final Folder Structure

```
web3py-simple-storage/
│
├── SimpleStorage.sol
├── deploy.py
├── SimpleStorage.json
├── venv/
└── README.md
```

---

## ✅ You’ve Learned

* Installing and using MetaMask, VSCode, Python, and Node.js
* Setting up Solidity environment with syntax highlighting
* Formatting and linting in VSCode
* Creating and running a Web3.py deployment script
* Basic VSCode shortcuts and developer workflow

---

## 📚 Next Steps

After setup:

1. Try deploying your contract to **Ganache** or a **testnet** (like Sepolia).
2. Read about **Web3.py contract functions** for interaction.
3. Learn about **Gas fees, Nonce, and Transactions**.

---

Would you like me to include a **sample `SimpleStorage.json`** (ABI + bytecode structure) for your Web3.py script so it runs without needing Remix export?
