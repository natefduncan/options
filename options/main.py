import click
import importlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from options.portfolio import Portfolio

def read_toml(path: str):
    with open(path, "rb") as f:
        toml_dict = tomllib.load(f)
    return toml_dict

def parse_toml(toml_dict) -> Portfolio:
    contracts = []
    for contract in toml_dict.get("contracts"):
        contract_type = contract.pop("type")
        if contract_type:
            module = importlib.import_module("options.contracts")
            cls = getattr(module, contract_type)
            contracts.append(cls(**contract))
        else:
            raise ValueError("Could not find contract type specification in toml file.")
    return Portfolio(toml_dict["title"], contracts)

def portfolio_from_path(path: str):
    return parse_toml(read_toml(path))

@click.group()
def cli():
    pass

@click.command()
@click.argument("path")
def parity_graph(path):
    p = portfolio_from_path(path)
    click.echo(p)

cli.add_command(parity_graph)

if __name__=="__main__":
    cli()
