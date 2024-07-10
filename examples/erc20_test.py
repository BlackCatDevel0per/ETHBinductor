from __future__ import annotations

import json
from os import environ
from pathlib import Path

from eth_erc20_bind import erc20
from web3 import Web3

wallet_private_key = environ['ETH_WPK']

RPC_URL = 'https://eth.llamarpc.com'

# erc20 contract addr
CADDR = '0xc3761eb917cd790b30dad99f6cc5b4ff93c4f9ea'


if __name__ == '__main__':
	with open(Path(Path(__file__).parent, 'abi/erc20.json'), 'r') as f:  # noqa: UP015
		abi = json.load(f)

	w3 = Web3(Web3.HTTPProvider(RPC_URL))
	ac = w3.eth.account.from_key(wallet_private_key)
	print(ac.address)
	c = erc20(web3=w3, contract_addr=CADDR, abi=abi)

	# print(c.name())
	print(c.balanceOf(ac.address))
