# Solidity Examples: BasicSolidity & SimpleStorage

This project demonstrates fundamental Solidity concepts such as variables, structs, arrays, mappings, functions, storage, and deploying smart contracts.

---

## 📌 Files

* **`BasicSolidity.sol`**
  Covers:

  * Versioning & SPDX license
  * Contract declaration
  * Types & declaring variables (`uint256`, `int256`, `bool`, `string`, `address`, `bytes32`)
  * Default initializations
  * Structs
  * Arrays (dynamic)
  * Mappings
  * Functions (state-changing examples: `addNumber`, `deposit`)
  * Intro to storage, scope, visibility

* **`SimpleStorage.sol`**
  Covers:

  * State variables and storage
  * Structs and arrays
  * Mappings
  * Public and view functions (`store`, `retrieve`, `addPerson`)
  * Example of state-changing and read-only functions

---

## ⚙️ How to Compile and Deploy

You can use **Remix IDE** ([https://remix.ethereum.org/](https://remix.ethereum.org/)) to compile and deploy both contracts.

### Steps:

1. Open [Remix IDE](https://remix.ethereum.org/).
2. Create two new files inside your workspace:

   * `BasicSolidity.sol`
   * `SimpleStorage.sol`
3. Paste the respective code into each file.
4. In the **Solidity Compiler** tab:

   * Select compiler version `0.8.30` (or `^0.8.0`).
   * Click **Compile BasicSolidity.sol** or **Compile SimpleStorage.sol**.
5. In the **Deploy & Run Transactions** tab:

   * Choose `BasicSolidity` or `SimpleStorage` from the contract dropdown.
   * Click **Deploy**.
6. After deploying:

   * For `BasicSolidity`:

     * Call `addNumber(10)` to add numbers into the array.
     * Call `deposit(100)` to increase your balance in the mapping.
   * For `SimpleStorage`:

     * Call `store(42)` to update `favoriteNumber`.
     * Call `retrieve()` to read it back.
     * Call `addPerson("Alice", 25)` to add a new entry to the people list.

---

## 📊 Data Flow Diagram

### `BasicSolidity.sol`

```
 User
   │
   ├── addNumber(10) ───────────▶ numbers[] (dynamic array)
   │
   └── deposit(100) ───────────▶ balances[msg.sender] (mapping)
```

### `SimpleStorage.sol`

```
 User
   │
   ├── store(42) ──────────────▶ favoriteNumber (uint256)
   │
   ├── retrieve() ◀───────────── favoriteNumber (returns value)
   │
   └── addPerson("Alice", 25) ─▶ people[] (array of struct)
                                 │
                                 └── nameToFavoriteNumber["Alice"] = 25 (mapping)
```

---

## ✅ Recap

* **BasicSolidity** introduces variables, structs, arrays, mappings, and functions.
* **SimpleStorage** focuses on storage, retrieval, mappings, and struct interactions.
* Both contracts are beginner-friendly building blocks for understanding Solidity and Ethereum smart contracts.

---