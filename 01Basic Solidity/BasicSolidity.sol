// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

contract BasicSolidity {
    // Variables
    bool public myBool = true;
    uint256 public myUint = 100;
    int256 public myInt = -50;
    string public myString = "Hello Solidity";
    address public myAddress = 0xBA19ab508f4a7D62aE8f48Fe4C8F2Cbef55A7bd5;
    bytes32 public myBytes = "cat";

    // Struct
    struct Person {
        string name;
        uint256 age;
    }
    Person public student = Person("Alice", 22);

    // Array
    uint256[] public numbers;

    // Mapping
    mapping(address => uint256) public balances;

    // Example Functions
    function addNumber(uint256 _num) public {
        numbers.push(_num);
    }

    function deposit(uint256 _amount) public {
        balances[msg.sender] += _amount;
    }
}
