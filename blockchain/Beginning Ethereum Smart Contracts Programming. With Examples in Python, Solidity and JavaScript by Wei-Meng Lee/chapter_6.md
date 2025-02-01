## Getting Started with Smart Contract


Smert Contract (Solidity) -> bytecode
ABI (application binary interface)

IDE/ remix IDE http://remix.ethereum.org/
(not the same any more, and current remix default Solidity version start with 0.8.1 , you change that)


## basic

contract // like class in java
function
returns
pure // will not change the value of state variables ,, need no gas to call



[
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "num1",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "num2",
				"type": "uint256"
			}
		],
		"name": "arithmetics",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "sum",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "product",
				"type": "uint256"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "num1",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "num2",
				"type": "uint256"
			}
		],
		"name": "multiply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	}
]
