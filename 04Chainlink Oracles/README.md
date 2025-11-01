# Chainlink Oracle Data Feed Project

---

### 📖 Definition

This project shows how a **smart contract fetches real-world ETH/USD prices** using **Chainlink’s decentralized oracle network**.
Blockchains can’t directly access off-chain data such as API prices or web data because they’re **closed systems**.
**Chainlink** solves this problem through **oracles** — independent nodes that bring verified external data onto the blockchain.

---

### 🧠 Concepts Covered

| Topic                                    | Description                                                                                             |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Chainlink Oracle Network**             | A decentralized group of nodes that collect, verify, and deliver data (like prices) to smart contracts. |
| **Why APIs Don’t Work Directly**         | Smart contracts can’t make HTTP requests because of blockchain isolation.                               |
| **Centralized vs Decentralized Oracles** | Centralized oracles can be manipulated; Chainlink uses multiple nodes to ensure trust and accuracy.     |
| **data.chain.link**                      | The official Chainlink data feed explorer showing live on-chain prices and oracle activity.             |
| **Price Feed Example**                   | Using Chainlink to get live ETH/USD price directly from a verified price feed contract.                 |

---

### 📂 Files

| File                  | Description                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| **ChainLinkFund.sol** | Solidity smart contract that retrieves and returns live ETH/USD price from Chainlink’s Sepolia testnet feed. |

---

### ⚙️ How It Works

1. The contract imports `AggregatorV3Interface` from the official Chainlink library.
2. The constructor connects the contract to the **ETH/USD price feed** on the **Sepolia testnet**.
3. The `getLatestPrice()` function:

   * Calls `latestRoundData()` from Chainlink’s oracle contract.
   * Extracts the `price` value.
   * Divides it by `1e8` to remove the default 8 decimal places.
   * Returns the **human-readable ETH/USD price** (e.g., `2435`).

---

### 🧩 Example Output

When you call:

```
getLatestPrice()
→ 2435
```

It means **1 ETH ≈ $2,435 USD**.
(Chainlink’s oracle originally returns prices with 8 decimals, which this function removes.)

---

### 🌍 Chainlink Price Feed Address

| Network                      | Feed    | Address                                      |
| ---------------------------- | ------- | -------------------------------------------- |
| **Ethereum Sepolia Testnet** | ETH/USD | `0x694AA1769357215DE4FAC081bf1f309aDC325306` |

*(Official reference: [Chainlink Docs – Price Feed Addresses](https://docs.chain.link/data-feeds/price-feeds/addresses?page=1&testnetPage=2#sepolia-testnet))*

---

### 🧰 How to Run in Remix IDE

#### Step 1 — Open Remix

Go to [https://remix.ethereum.org](https://remix.ethereum.org)

#### Step 2 — Create File

Create a new file named **`ChainLinkFund.sol`** and paste the contract code.

#### Step 3 — Compile

1. Open the **Solidity Compiler** tab.
2. Set compiler version to **0.8.0 or higher**.
3. Click **Compile ChainLinkFund.sol**.

#### Step 4 — Connect MetaMask

1. Go to the **Deploy & Run Transactions** tab.
2. Under **Environment**, select **Injected Provider – MetaMask**.
3. Connect MetaMask to **Sepolia Testnet**.
4. Get some test ETH from a **Sepolia faucet**.

#### Step 5 — Deploy

1. No constructor parameters are required (feed address is hardcoded).
2. Click **Deploy** and confirm the transaction.

#### Step 6 — Fetch Price

1. After deployment, expand the **Deployed Contract** section.
2. Click **getLatestPrice()**.
3. You’ll see the live ETH/USD price from Chainlink’s oracle.

---

### 📝 Recap

✅ **Key Points**

* Smart contracts can’t access external data by default.
* Chainlink oracles securely bring off-chain data (like prices) on-chain.
* `AggregatorV3Interface` is the standard way to read decentralized data feeds.
* This contract simplifies the price by removing extra decimals for clarity.

---

### 💡 Optional Challenge

Try extending the contract to:

* Convert **ETH to USD** by multiplying an input ETH amount with the live price.
* Add an **event** to log fetched prices on-chain.
* Support multiple feeds (e.g., BTC/USD, LINK/USD) via constructor input.

---