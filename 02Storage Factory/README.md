# Storage Factory Project

## 📖 Definition

This project demonstrates three important Solidity concepts:

* **Factory Pattern**
  A contract (`StorageFactory`) that can **deploy and manage multiple other contracts** (`SimpleStorage`).

* **Inheritance**
  `ExtraStorage` inherits from `SimpleStorage` and overrides the `store` function to add custom logic.

* **Interacting with External Contracts**
  `StorageFactory` interacts with `SimpleStorage` contracts it has deployed.

---

## 📂 Files

* `SimpleStorage.sol` → Basic contract to store/retrieve a number and track people’s favorite numbers.
* `StorageFactory.sol` → Deploys `SimpleStorage` contracts and interacts with them.
* `ExtraStorage.sol` → Inherits from `SimpleStorage` and overrides the `store` function.

---

## ⚙️ How to Compile and Deploy

### 1. Open Remix IDE

* Go to [https://remix.ethereum.org](https://remix.ethereum.org)

### 2. Create Files

* Create three new files inside Remix:

  * `SimpleStorage.sol`
  * `StorageFactory.sol`
  * `ExtraStorage.sol`
* Copy the respective contract code into each file

### 3. Compile

* In the **Solidity Compiler** tab:

  * Use version **0.8.7** (or any `^0.8.x` version)
  * Compile each file

### 4. Deploy

* In the **Deploy & Run Transactions** tab:

  * Deploy **`StorageFactory`** (this is the main contract)

---

## 🚀 How to Run

1. **Create a SimpleStorage contract**

   * Call `createSimpleStorageContract()` inside `StorageFactory`
   * This deploys a new `SimpleStorage` instance and stores it in `simpleStorageArray`

2. **Store a number**

   * Call `sfStore(0, 123)`

     * `0` = index of the deployed `SimpleStorage` in the array
     * `123` = number to store

3. **Retrieve the number**

   * Call `sfGet(0)`
   * You should see `123` returned

4. **Deploy ExtraStorage (optional)**

   * Deploy **`ExtraStorage`** separately
   * Call `store(50)`
   * It will save `50 + 5 = 55` because the function is overridden

---

## 📝 Recap

* `SimpleStorage` → basic contract with store/retrieve logic
* `StorageFactory` → factory pattern to deploy and interact with many `SimpleStorage` contracts
* `ExtraStorage` → inheritance + function override example

---