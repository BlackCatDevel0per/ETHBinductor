from __future__ import annotations
from typing import TYPE_CHECKING
from ethbind import ETHABIBindBase
if TYPE_CHECKING:
    from typing import Any
    from ethbind.types import bytes32, uint8, uint16, uint64, uint256, fee, sequence


class erc20(ETHABIBindBase):

    def name(self) -> str:
        return self.contract.functions.name().call()

    def approve(self, _spender: Any, _value: uint256) -> bool:
        return self.contract.functions.approve(_spender, _value).call()

    def totalSupply(self) -> uint256:
        return self.contract.functions.totalSupply().call()

    def transferFrom(self, _from: Any, _to: Any, _value: uint256) -> bool:
        return self.contract.functions.transferFrom(_from, _to, _value).call()

    def decimals(self) -> uint8:
        return self.contract.functions.decimals().call()

    def burn(self, _value: uint256) -> bool:
        return self.contract.functions.burn(_value).call()

    def balanceOf(self, value: Any) -> uint256:
        return self.contract.functions.balanceOf(value).call()

    def burnFrom(self, _from: Any, _value: uint256) -> bool:
        return self.contract.functions.burnFrom(_from, _value).call()

    def symbol(self) -> str:
        return self.contract.functions.symbol().call()

    def transfer(self, _to: Any, _value: uint256) ->None:
        return self.contract.functions.transfer(_to, _value).call()

    def approveAndCall(self, _spender: Any, _value: uint256, _extraData: str
        ) -> bool:
        return self.contract.functions.approveAndCall(_spender, _value,
            _extraData).call()

    def allowance(self, value_0: Any, value_1: Any) -> uint256:
        return self.contract.functions.allowance(value_0, value_1).call()

# Generated by ETHBinductor: https://github.com/BlackCatDevel0per/ETHBinductor
