// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// Import Chainlink's AggregatorV3Interface to read live data feeds
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract PriceConsumerV3 {
    // Declare a variable for the price feed
    AggregatorV3Interface internal priceFeed;

    // Set the Chainlink price feed address during deployment
    constructor(address _priceFeedAddress) {
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    // Get the latest ETH/USD price from Chainlink Oracle
    function getLatestPrice() public view returns (int) {
        (
            , 
            int price,
            ,
            ,
        ) = priceFeed.latestRoundData();
        return price; // Example: 250000000000 = $2,500.00
    }
}
