from __future__ import annotations

from typing import TYPE_CHECKING, NewType

if TYPE_CHECKING:
	...

# Contract functions & types

bytes32 = NewType('bytes32', int)

uint8 = NewType('uint8', int)
uint16 = NewType('uint16', int)
uint64 = NewType('uint64', int)
uint256 = NewType('uint256', int)

address = NewType('address', str)


# fee = NewType('fee', uint256)
# sequence = NewType('sequence', uint64)
