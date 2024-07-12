from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from typing import Any


def get_json(filepath: str) -> list[dict[str, Any]]:
	with open(filepath, 'r') as f:  # noqa: UP015
		return json.loads(f.read())
