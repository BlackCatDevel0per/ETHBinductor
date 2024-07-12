from ethbinductor.providers.output.output_base import out_base


@out_base
def put(data: str, output: str) -> None:
	with open(output, 'w') as f:
		f.write(data)
