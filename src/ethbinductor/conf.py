from __future__ import annotations

import ast
from ast import Module
from pathlib import Path
from typing import TYPE_CHECKING

from ethbind.types import __file__ as ethbbf

from ethbinductor.utils import defdict

if TYPE_CHECKING:
	from typing import Final


_TEST_ETH_ADDR: str = '0xeD70EF0f4c9245199dE59989BB78D7b9Cf82932a'
_TEST_ETH_ERC20_ADDR: str = '0xc3761eb917cd790b30dad99f6cc5b4ff93c4f9ea'

_TYPES_ABI2PY: dict[str, str] = {
	'bool': 'bool',
	'string': 'str',
	'bytes': 'str',##int|str??

	# TODO: Split this part to the new one..
	# or make managed sequence..
	# internal (Python only)
	'dict[str, Any]': 'dict[str, Any]',
}


def _dfact(key: str) -> str:
	# FIXME: Do logging!
	print(f'[WARNING] Unknown type `{key}`')
	return 'Any'


TYPES_ABI2PY: Final[dict[str, str]] = defdict(_dfact)  # type: ignore
TYPES_ABI2PY.update(_TYPES_ABI2PY)

MDIR: Final[Path] = Path(__file__).parent

# Read the bind base sample
with open(Path(MDIR, 'samples', 'BindBase.py')) as _bbf:
	abi_sample: str = _bbf.read()
del _bbf

abi_sample_module_tree: Module = ast.parse(abi_sample)
for index, node in enumerate(abi_sample_module_tree.body):
	if isinstance(node, ast.ClassDef):
		break
BB_cls_index: Final[int] = index
del index
# del `pass`
del abi_sample_module_tree.body[BB_cls_index].body[0]
abi_sample_module_tree.body[3].body[1].names.clear()

# Append type imports instead of `*`
with open(ethbbf, 'r') as _ethbbf_f:
	_ethbbf_tree = ast.parse(_ethbbf_f.read())

_TYPES_ABI2PY_ALTS: Final[list[str]] = []

_node: ast.Assign
for _node in _ethbbf_tree.body:
	if not isinstance(_node, ast.Assign):
		continue
	first_varn: str = _node.targets[0].id
	_TYPES_ABI2PY_ALTS.append(first_varn)
	abi_sample_module_tree.body[3].body[1].names.append(
		ast.alias(name=first_varn, asname=None),
	)

TYPES_ABI2PY.update(zip(_TYPES_ABI2PY_ALTS, _TYPES_ABI2PY_ALTS, strict=True))

##
# print(vars(abi_sample_module_tree.body[3].body[1]))
# print(abi_sample_module_tree.body[3].body[1].names)
# print(vars(abi_sample_module_tree.body[BB_cls_index].body[0].returns))
# exit()
