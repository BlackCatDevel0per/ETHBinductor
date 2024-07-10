from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from collections.abc import Callable
	from typing import Any


class defdict(defaultdict):
	default_factory: Callable[[Any], Any]  # type: ignore

	def __missing__(self: defdict, key: Any) -> Any:
		return self.default_factory(key)
