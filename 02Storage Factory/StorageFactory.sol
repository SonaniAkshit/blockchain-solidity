// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./SimpleStorage.sol";

contract StorageFactory {
    SimpleStorage[] public storageArray;
  
    function createSimpleStorage() public {
        SimpleStorage s = new SimpleStorage();
        storageArray.push(s);
    }

    function setNumberInStorage(uint256 index, uint256 _num) public {
        SimpleStorage s = storageArray[index];
        s.setNumber(_num);
    }

    function getNumberFromStorage(uint256 index) public view returns (uint256) {
        SimpleStorage s = storageArray[index];
        return s.number();
    }

    function countSimpleStorages() public view returns (uint256) {
        return storageArray.length;
    }
}