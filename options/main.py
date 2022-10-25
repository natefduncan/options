import click
import importlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

from options.portfolio import Portfolio
from options.contracts import Position
from options.pricing import BlackScholes

def read_toml(path: str):
    with open(path, "rb") as f:
        toml_dict = tomllib.load(f)
    return toml_dict

def parse_toml(toml_dict) -> Portfolio:
    contracts = []
    for contract in toml_dict.get("contracts"):
        contract_type = contract.pop("type")
        contract["position"] = Position.BUY if contract["position"] == "BUY" else Position.SELL
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
@click.option("--underlying-max", default=100)
def parity_graph(path, underlying_max):
    p = portfolio_from_path(path)
    p.parity_graph(underlying_max)

@click.command()
@click.argument("path")
@click.option("--x-axis", "-x", default="volatility")
@click.option("--y-axis", "-y", default="contract_price")
def info_graph(path, x_axis, y_axis):
    p = portfolio_from_path(path)
    p.info_graph(x_axis, y_axis)

cli.add_command(parity_graph)
cli.add_command(info_graph)

if __name__=="__main__":
    cli()
