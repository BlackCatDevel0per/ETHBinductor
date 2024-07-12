from __future__ import annotations

from typing import TYPE_CHECKING

from ethbinductor.conf import _TEST_ETH_ERC20_ADDR
from ethbinductor.providers.abi.http_base import base_get_json

if TYPE_CHECKING:
	from typing import Any, Final


ABI_ENDPOINT = 'https://api.etherscan.io/api'

REQ_DATA: Final[dict[str, Any]] = {
	'module': 'contract',
	'action': 'getabi',
	'address': '',
}


def get_json(
	addr: str, *,
	endpoint: str = ABI_ENDPOINT, data: dict[str, Any] = REQ_DATA,
	**rkw: Any,
) -> list[dict[str, Any]]:
	return base_get_json(addr, endpoint=endpoint, data=data.copy())


if __name__ == '__main__':
	import json

	result: list[dict[str, Any]] = get_json(_TEST_ETH_ERC20_ADDR)
	# to validate
	abi = json.dumps(result, indent=4, ensure_ascii=False)
	print(abi)
