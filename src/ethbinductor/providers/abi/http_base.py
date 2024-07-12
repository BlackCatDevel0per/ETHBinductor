from __future__ import annotations

import json
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
	from typing import Any


class JSONDecodeErr(Exception):
	pass


def base_get_json(
	addr: str, *,
	addr_key: str = 'address',
	resp_key: str = 'result',
	def_status_code: int = 200,
	endpoint: str, data: dict[str, Any],
	**rkw: Any,
) -> list[dict[str, Any]]:
	data[addr_key] = addr
	response = requests.post(endpoint, data, **rkw)
	try:
		response_json = response.json()
	except requests.exceptions.JSONDecodeError as err:
		msg = f'Text: `{response.text}`'
		if len(response.text) < 350:  # noqa: PLR2004
			raise JSONDecodeErr(msg) from err
		raise JSONDecodeErr(msg[0:350] + '...') from err
	if response.status_code != def_status_code:
		# Not the best exception class, but..
		msg = f'Invalid response, code: {response.status_code}, text: `{response.text}`'
		if len(response.text) < 350:  # noqa: PLR2004
			raise requests.exceptions.HTTPError(msg)
		raise requests.exceptions.HTTPError(msg[0:350] + '...')

	return json.loads(response_json[resp_key])
