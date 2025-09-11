# BasicSolidity Contract

## 📖 Definition

This project contains a simple Solidity smart contract that demonstrates the **basic building blocks** of Ethereum development. It covers:

* **Variables / Data Types**

  * `bool` → true/false values
  * `uint256` → unsigned integer (positive numbers)
  * `int256` → signed integer (positive and negative numbers)
  * `string` → text values
  * `address` → Ethereum account or contract address
  * `bytes32` → fixed-length 32-byte data

* **Structs** → Custom data type grouping multiple values

* **Arrays** → Fixed or dynamic lists of elements

* **Mappings** → Key-value storage (like a dictionary)

* **Functions** → Read and update contract state

---

## 📂 File

* `BasicSolidity.sol`

---

## ⚙️ How to Compile and Deploy

### 1. Open Remix IDE

* Go to [https://remix.ethereum.org](https://remix.ethereum.org)

### 2. Create File

* In Remix, create a new file called **`BasicSolidity.sol`**
* Copy and paste the contract code from this repo into the file

### 3. Compile

* In the **Solidity Compiler** tab:

  * Select **version 0.8.30** (or the closest available ≥0.8.0)
  * Click **Compile BasicSolidity.sol**

### 4. Deploy

* Go to the **Deploy & Run Transactions** tab
* Select **Environment**:

  * `JavaScript VM` (local in-browser blockchain, free ETH)
  * or `Injected Provider` (MetaMask) if you want to deploy on a real/test network
* Click **Deploy**
* Contract will appear under **Deployed Contracts**

### 5. Interact

* Expand your deployed contract in Remix
* Try these functions:

  * `myUint`, `myString`, `myAddress` → Read public variables
  * `addNumber(10)` → Add number to array
  * `deposit(50)` → Deposit tokens to your balance
  * `balances(msg.sender)` → Check your balance
---

# SimpleStorage Contract

## 📖 Definition

This contract is a beginner-friendly **Solidity smart contract** that allows you to:

* **Store and retrieve a number**
* **Create a list of people** (with name and favorite number)
* **Use a mapping** to quickly look up a person’s favorite number by their name

It demonstrates:

* State variables (`favoriteNumber`)
* Structs (`People`)
* Dynamic arrays (`people`)
* Mappings (`nameToFavoriteNumber`)
* Functions (`store`, `retrieve`, `addPerson`)

---

## 📂 File

* `SimpleStorage.sol`

---

## ⚙️ How to Compile and Deploy

### 1. Open Remix IDE

* Go to [https://remix.ethereum.org](https://remix.ethereum.org)

### 2. Create File

* In Remix, create a new file called **`SimpleStorage.sol`**
* Copy and paste the contract code into this file

### 3. Compile

* In the **Solidity Compiler** tab:

  * Choose version **0.8.30** (or a compatible `^0.8.x`)
  * Click **Compile SimpleStorage.sol**

### 4. Deploy

* Go to the **Deploy & Run Transactions** tab
* Select **Environment**:

  * `JavaScript VM` (local, free ETH for testing)
  * or `Injected Provider` (e.g., MetaMask) to deploy on a real/test network
* Click **Deploy**
* Contract will appear under **Deployed Contracts**

---

## 🚀 How to Interact

Once deployed, expand the contract in Remix and try these:

* **`store(uint256)`** → Save a favorite number
* **`retrieve()`** → View the stored number
* **`addPerson(string, uint256)`** → Add a new person with their name and favorite number
* **`people(uint index)`** → Get a person by index (from the `people` array)
* **`nameToFavoriteNumber(string)`** → Look up a favorite number by person’s name

---

## 📊 Flowchart (Logic Overview)

```markdown
flowchart TD
    A[store(uint256)] -->|sets| B[favoriteNumber]
    C[retrieve()] -->|returns| B

    D[addPerson(string, uint256)] --> E[people array]
    D --> F[nameToFavoriteNumber mapping]

    E -->|index| G[People{name, favoriteNumber}]
    F -->|lookup by name| H[favoriteNumber]
```

---