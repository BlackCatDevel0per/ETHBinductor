from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from web3 import Web3
	from web3.contract.contract import ChecksumAddress, Contract, ContractEvents, ContractFunctions


class ETHABIBindBase:

	def __init__(
		self: ETHABIBindBase,
		web3: Web3,
		contract_addr: ChecksumAddress,
		abi: dict,
	) -> None:
		self.web3: Web3 = web3
		self.contract: Contract = self.web3.eth.contract(
			self.web3.to_checksum_address(contract_addr), abi=abi,  #
		)

		self.functions: ContractFunctions = self.contract.functions
		self.events: ContractEvents = self.contract.events
