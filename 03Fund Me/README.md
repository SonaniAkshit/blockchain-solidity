# FundMe Contract

## 📖 Definition

This project demonstrates **payable functions**, handling **Ether transfers**, and using **`msg.sender`** and **`msg.value`** in Solidity.

### Key Concepts Covered:

* **Payable**: Functions marked `payable` can receive Ether.
* **Units of Measure**: Solidity supports `wei`, `gwei`, and `ether` for readability.

  * `1 ether = 10^18 wei`
  * `1 gwei = 10^9 wei`
* **msg.sender**: Address of the account or contract that called the function.
* **msg.value**: Amount of Ether sent with a payable function call.

---

## 📂 File

* `FundMe.sol` → A contract that allows users to fund it with Ether, tracks contributions, and lets the deployer withdraw the balance.

---

## ⚙️ How to Compile and Deploy

### 1. Open Remix IDE

* Go to [https://remix.ethereum.org](https://remix.ethereum.org).

### 2. Create File

* Create a new file called **`FundMe.sol`**.
* Paste the contract code inside.

### 3. Compile

* Open the **Solidity Compiler** tab.
* Select compiler version `0.8.20` (or higher `^0.8.x`).
* Click **Compile FundMe.sol**.

### 4. Connect MetaMask

1. Install the **MetaMask extension** in your browser and create/import a wallet.
2. Add some test ETH (using a faucet if you are on a testnet).
3. In Remix → go to **Deploy & Run Transactions** tab.
4. Change **Environment** to `Injected Provider - MetaMask`.
5. MetaMask will ask for confirmation → approve the connection.
6. Now Remix is connected to your MetaMask account.

### 5. Deploy

* Select **FundMe** from the contract dropdown.
* Click **Deploy**.
* MetaMask will pop up → confirm the transaction.

---

## 🚀 How to Run

1. **Fund the contract**

   * In Remix, enter at least **0.01 ETH** in the **Value** field.
   * Call the `fund()` function.
   * This will update `addressToAmountFunded[msg.sender]` and add your address to `funders`.

2. **Check contract balance**

   * Call `getBalance()` to see how much Ether is stored in the contract.

3. **Withdraw funds**

   * Call `withdraw()`.
   * All funds are transferred to the caller’s address (`msg.sender`).
   * MetaMask will ask for confirmation → approve it.

---

## 📊 Example Flow

```
User (msg.sender)
   │ sends 0.02 ETH
   ▼
 fund() [payable]
   │
   ├── stores contribution in mapping
   ├── records sender in funders array
   └── updates contract balance

Contract balance can be:
   ├── checked with getBalance()
   └── withdrawn with withdraw() → funds go to caller
```

---

## 📝 Recap

* `fund()` accepts ETH via `payable`.
* `msg.sender` identifies the contributor.
* `msg.value` is the amount of ETH sent.
* `getBalance()` shows contract’s ETH balance.
* `withdraw()` transfers all ETH to the caller.
* **MetaMask** enables real deployment on testnets or mainnet.

---