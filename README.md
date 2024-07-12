## ETHBinductor (ETH Contract abi Bind Conductor)

This tool helps to generate web3py bind of etherium contract abi from abi json.

### Installation:
```bash
pip install ethbinductor
```

Additional lib for binds:
```bash
pip install ethbind
```

### Usage:

#### Run cli:
```bash
python -m ethbinductor
```
or
```bash
python3 -m ethbinductor
```
else
```bash
ethbinductor
```

#### Parse abi & get using abi providers:
```bash
# Contract (ERC20) load using etherscan http json api (default output to console)
ethbinductor get-abi 0xc3761eb917cd790b30dad99f6cc5b4ff93c4f9ea --abi-provider etherscan
```

##### Save json abi into the file (more providers see in the sources & cli help)
```bash
# Contract (ERC20) load using etherscan http json api (save to file)
ethbinductor get-abi 0xc3761eb917cd790b30dad99f6cc5b4ff93c4f9ea --abi-provider etherscan --output file examples/abi/erc20.json
```

#### Translate json abi to the code bind:
```bash
# Contract (ERC20) load using file & translate it to native Python binding (default output to console)
ethbinductor abi2py --cls-name ERC20 --abi-provider file examples/abi/erc20.json
```

```bash
# Same, but save translated code to file
ethbinductor abi2py --cls-name ERC20 --abi-provider file examples/abi/erc20.json --output file examples/eth_erc20_bind.py
```

```bash
# Contract (ERC20) load using etherscan & translate it to native Python binding (default output to console)
ethbinductor abi2py --cls-name ERC20 --abi-provider etherscan 0xc3761eb917cd790b30dad99f6cc5b4ff93c4f9ea
```

##### Save Python bind into the file (more providers see in the sources & cli help)
```bash
# Contract (ERC20) load using etherscan & translate it to native Python binding (save to file)
ethbinductor abi2py --cls-name ERC20 --abi-provider etherscan 0xc3761eb917cd790b30dad99f6cc5b4ff93c4f9ea --output file examples/eth_erc20_bind.py
```

Bind example of ERC20 you can see [here](examples/eth_erc20_bind.py) with usage [example](examples/erc20_test.py) but, first install base lib:
```bash
pip install ethbind
```

##### TODO: Custom samples & providers (for example to use bscscan with your api key & etc.)

[//]: # (TODO: Jinja2 sampling, [Optional] Pydantic type checks, other cli tools.. & rename some files..)
