from __future__ import annotations

import ast
from typing import TYPE_CHECKING

from ethbinductor.conf import TYPES_ABI2PY

if TYPE_CHECKING:
	from typing import Any


def _fargs_parse(fargs: list[dict[str, str]]) -> list[tuple[str, str]]:
	fargs_len = len(fargs)
	# TODO: ... some additional stuff ...
	if fargs_len > 1:
		args = [
			(arg['name'] if arg['name'] else f'value_{num}', arg['type'])
			for num, arg in enumerate(fargs)
		]
	elif fargs_len == 1:
		_argin = fargs[0]
		args = [(_argin['name'] if _argin['name'] else 'value', _argin['type'])]
		del _argin
	else:
		args = []

	return args


def create_def_node(func: dict[str, Any]) -> ast.FunctionDef:
	func_name = func['name']
	inputs = func['inputs']
	outputs = func['outputs']
	# state_mutability = func['stateMutability']

	# # Args
	# Parse args
	args: list[tuple[str, str]] = _fargs_parse(inputs)

	# TODO: Option to replace/format arg name

	# Make def node
	args_node = ast.arguments(
		args=['self'] + [
			ast.arg(
				arg=aname,  # FIXME: Flag if noname arg..
				annotation=ast.Name(id=TYPES_ABI2PY[atype]),
			) for aname, atype in args
		],
		vararg=None, kwarg=None, defaults=[],
		# kwonlyargs=[],
		# kw_defaults=[],
	)

	# # Contract func call
	call_args = [ast.Name(id=aname) for aname, _ in args]
	# TODO: Find ways to detect "read" & write funcs..
	# `self.contract.functions.<func_name>.call()` - read func..
	val = ast.Call(
		func=ast.Attribute(
			value=ast.Call(
				# self.contract.functions.<func_name>
				func=ast.Attribute(
					# self.contract
					value=ast.Attribute(
						value=ast.Name(
							id='self',
						),
						attr='contract',
					),
					attr='functions.' + func_name,
				),
				args=call_args,
				keywords=[],
			),
			attr='call',
			# TODO: Transaction generate by some info.. (`.build_transaction` method)
		),

		# empty call, aka: `.call()`
		args=[],
		keywords=[],
	)

	# # FIXME: Move it to the other place!
	# # Transact (if need)
	# if call_args:
	# 	val = ast.Call(
	# 		func=ast.Attribute(value=contract_func_call, attr='transact'),
	# 		args=[ast.Dict(
	# 			keys=[ast.Str(s='from'), ast.Str(s='gas')],
	# 			values=[ast.Name(id='from_address'), ast.Name(id='gas')]
	# 		)],
	# 		keywords=[],
	# 	)
	# else:
	# 	val = contract_func_call

	return_node = ast.Return(value=val)

	body = [return_node]
	outs_len = len(outputs)
	rets: 'ast.Name | ast.Subscript | ast.Constant'
	if outs_len == 1:
		# just one return type
		rets = ast.Name(id=' ' + TYPES_ABI2PY[outputs[0]['type']])
	elif outs_len > 1:
		# tuple of return types
		rets = ast.Subscript(
			value=ast.Name(id='tuple'),
			slice=ast.Tuple(
				elts=[
					ast.Name(
						id=' ' + TYPES_ABI2PY[out['type']],
					) for out in outputs
				],
			),
		)
	elif outs_len == 0:
		# return None
		# FIXME: Add space without literlly strs concat like: `' ' + svar`.. use simple formatter..
		rets = ast.Constant(value=None, kind=None)


	function_node = ast.FunctionDef(
		name=func_name,
		args=args_node,
		body=body,
		decorator_list=[],
		returns=rets,
	)

	return function_node
