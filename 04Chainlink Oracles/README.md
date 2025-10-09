# Chainlink Oracle Data Feed Project

---

### 📖 Definition

This project demonstrates how **smart contracts get real-world data** using **Chainlink Oracles**.
Normally, **blockchains cannot access external data (like stock prices or APIs)** because they are closed systems.
**Chainlink** solves this by providing a **decentralized network of oracles** that securely deliver data on-chain.

---

### 🧠 Concepts Covered

| Topic                                    | Description                                                                                                |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Chainlink Oracle Network**             | A decentralized group of nodes that fetch and verify real-world data before sending it to smart contracts. |
| **Why APIs Don’t Work Directly**         | Smart contracts can’t make HTTP calls due to blockchain isolation, so they need oracles.                   |
| **Centralized vs Decentralized Oracles** | Centralized oracles can fail or be manipulated; Chainlink prevents this by using multiple nodes.           |
| **data.chain.link**                      | The official Chainlink data feed explorer for live on-chain prices.                                        |
| **Price Feed Example**                   | Using Chainlink to get live ETH/USD prices directly in your Solidity contract.                             |

---

### 📂 Files

| File                    | Description                                                             |
| ----------------------- | ----------------------------------------------------------------------- |
| **PriceConsumerV3.sol** | Solidity contract that reads ETH/USD price using Chainlink oracle feed. |

---

### ⚙️ How It Works

1. The contract imports `AggregatorV3Interface` from Chainlink.
2. When deployed, it connects to a specific **Chainlink Price Feed contract** (like ETH/USD).
3. The `getLatestPrice()` function calls Chainlink’s on-chain data and returns the latest price.

---

### 🌍 Common Chainlink Price Feed Addresses

| Network              | ETH/USD Feed Address                         |
| -------------------- | -------------------------------------------- |
| **Ethereum Mainnet** | `0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419` |
| **Sepolia Testnet**  | `0x694AA1769357215DE4FAC081bf1f309aDC325306` |
| **Polygon Mainnet**  | `0xF9680D99D6C9589e2a93a78A04A279e509205945` |

---

### 🧩 Example Output

When you run the function:

```
getLatestPrice()
→ 285000000000
```

It means **1 ETH = $2,850.00**
(Chainlink feeds return prices with 8 decimals.)

---

### 🧰 How to Run in Remix IDE

#### Step 1 — Open Remix

Go to [https://remix.ethereum.org](https://remix.ethereum.org)

#### Step 2 — Create a File

Create a new file named **`PriceConsumerV3.sol`** and paste the contract code.

#### Step 3 — Compile

1. Click the **Solidity Compiler** tab.
2. Set the compiler version to **0.8.20**.
3. Click **Compile PriceConsumerV3.sol**.

#### Step 4 — Connect MetaMask

1. Open the **Deploy & Run Transactions** tab.
2. Under **Environment**, select **Injected Provider – MetaMask**.
3. Connect your MetaMask wallet to **Sepolia Testnet**.
4. Get some test ETH from a **Sepolia faucet** if needed.

#### Step 5 — Deploy the Contract

1. In the constructor input, enter the Chainlink feed address for Sepolia:

   ```
   0x694AA1769357215DE4FAC081bf1f309aDC325306
   ```
2. Click **Deploy**.
3. Confirm the MetaMask transaction.

#### Step 6 — Read the Price

1. After deploying, click **getLatestPrice()** under Deployed Contracts.
2. You’ll see the live ETH/USD price returned from the Chainlink Oracle.

---

### 📝 Recap

✅ **Key Takeaways**

* Blockchains can’t access external data by themselves.
* Chainlink Oracles bridge real-world data to smart contracts.
* The `AggregatorV3Interface` lets contracts read decentralized data feeds like prices.

---

### 💡 Optional Challenge

Try modifying the contract to:

* Convert **ETH to USD** using the live price.
* Display price with proper decimal formatting.
* Add an event to log new price updates.

---