# 🚀 AdvancedFundMe

## 📖 Definition

**AdvancedFundMe** is a Solidity-based crowdfunding contract that allows users to **send ETH**, **track contributions**, and **withdraw funds** securely.
It integrates **Chainlink Price Feeds** to fetch live ETH/USD prices and demonstrates several **advanced Solidity concepts**, including **mappings, dynamic arrays, modifiers, tuples, and safe ETH handling**.

---

## 🔑 Key Features

* 💰 **Fund the contract** by sending ETH
* 👥 **Track funders** and their total contributions
* 📈 **Fetch real-time ETH/USD price** using Chainlink oracles
* 💵 **Convert ETH to USD** dynamically using on-chain data
* 🔐 **Owner-only withdrawal** using safe `call` transfers
* ⚙️ Demonstrates key Solidity topics:

  * Mappings & dynamic arrays
  * Function modifiers
  * Tuple destructuring
  * Require/revert logic
  * Unit conversions (wei ↔ ether)
  * External oracle data integration

---

## 📂 File

**AdvancedFundMe.sol**
Smart contract implementing decentralized funding logic with real-time ETH/USD conversion using Chainlink oracles.

---

## ⚙️ How It Works

1. **Funding:**

   * Any user can call `fund()` and send ETH.
   * The amount is recorded in a **mapping** that tracks how much each address contributed.
   * The funder’s address is also stored in a **dynamic array** for easy iteration and resets.

2. **Price Feed Integration:**

   * The contract connects to the **Chainlink ETH/USD Price Feed** on the **Sepolia Testnet**.
   * The price feed returns ETH price data with 8 decimals, which is scaled to 18 decimals for accuracy.
   * `getVersion()` confirms the feed version.
   * `getPrice()` fetches the current ETH/USD value.

3. **ETH to USD Conversion:**

   * The function `getConversionRate(ethAmount)` converts any ETH amount into USD value based on the latest Chainlink price.
   * This is useful for calculating funding targets in fiat value.

4. **Withdrawal:**

   * Only the **owner** (the deployer) can call `withdraw()`.
   * It transfers the full contract balance safely using the `call` method.
   * After withdrawal, the contract resets all funder records and clears the funders array.

5. **Balance Checking:**

   * The `getBalance()` function shows the total ETH currently held in the contract.

---

## 🌍 Chainlink Oracle Information

| Network             | Feed    | Address                                      |
| ------------------- | ------- | -------------------------------------------- |
| **Sepolia Testnet** | ETH/USD | `0x694AA1769357215DE4FAC081bf1f309aDC325306` |

*(Official Source: [Chainlink Data Feed Addresses](https://docs.chain.link/data-feeds/price-feeds/addresses))*

---

## 🛠 How to Compile & Deploy

1. Open [**Remix IDE**](https://remix.ethereum.org/)
2. Create a new file named **`AdvancedFundMe.sol`**
3. Paste the contract code
4. Set compiler version to **0.8.x** and enable optimization
5. Click **Compile AdvancedFundMe.sol** ✅
6. Go to the **Deploy & Run Transactions** tab
7. Choose your environment:

   * **Injected Provider (MetaMask)** for testnets like Sepolia
   * **JavaScript VM** for local testing
8. Click **Deploy** 🚀
9. Confirm the transaction in MetaMask

---

## ⚡ How to Use

| Function                         | Description                                                           |
| -------------------------------- | --------------------------------------------------------------------- |
| **fund()**                       | Send ETH to the contract (must include value in Remix “Value” field). |
| **getBalance()**                 | View the total ETH currently stored in the contract.                  |
| **getPrice()**                   | Fetch the current ETH/USD price using Chainlink Oracle.               |
| **getConversionRate(ethAmount)** | Convert any ETH amount (in wei) into USD based on live price feed.    |
| **getVersion()**                 | Check the version of the Chainlink price feed used.                   |
| **withdraw()**                   | Withdraw all funds to the owner’s address (only owner can call).      |

---

## 🔄 Example Flow

1. **Deployment**

   * Owner deploys the contract on Sepolia testnet.

2. **Funding**

   * Alice calls `fund()` and sends 0.5 ETH.
   * Bob sends 1 ETH.
   * The mapping and array update with each contribution.

3. **Check Balance**

   * `getBalance()` returns the total ETH held.

4. **Conversion Example**

   * `getConversionRate(1e18)` → Returns USD value of 1 ETH.

5. **Withdraw**

   * Owner calls `withdraw()` → All ETH sent to owner, contributors reset.

---

## 🧠 Solidity Concepts Used

| Concept                    | Description                                                |
| -------------------------- | ---------------------------------------------------------- |
| **Mapping**                | Tracks how much ETH each address contributed.              |
| **Dynamic Array**          | Stores all funder addresses for resetting.                 |
| **Modifier**               | Restricts access to owner-only functions.                  |
| **Tuple Destructuring**    | Extracts values from Chainlink’s `latestRoundData()`.      |
| **Require & Revert**       | Ensures correct inputs and secure execution.               |
| **Safe Transfer via call** | Recommended method to send ETH in Solidity 0.8+.           |
| **Unit Conversion**        | Adjusts decimals between ETH (18) and Chainlink feeds (8). |

---

## 📝 Recap

✅ Demonstrates **real-world Solidity fundamentals** and **oracle integration**.
✅ Secure ETH funding and withdrawal using **best practices**.
✅ Live ETH/USD conversion powered by **Chainlink**.
✅ Clear separation between **user functions** and **owner privileges**.
✅ Ideal project for understanding **decentralized funding** and **price feed usage**.

---

## ⚠️ Notes

* Always deploy to **testnets (Sepolia, Goerli)** before mainnet.
* Use **MetaMask** for funding and testing.
* Keep private keys secure and avoid hardcoding sensitive data.
* Contract is for **educational and testing purposes** only — not audited for production.

---