from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from collections.abc import Callable


def out_base(func: Callable[[str, str], None]) -> Callable[[str, str], None]:
	def base(data: str, output: str) -> None:
		if output in ('-',):
			msg = 'Specify non-default value!'
			raise ValueError(msg)
		return func(data, output)

	return base
