from typing import List
from options.contracts import *

class Portfolio:

    def __init__(self, name: str, contracts: List[Contract]):
        self.name = name
        self.contracts = contracts

    def __repr__(self):
        return f"{self.name}:\n" + "\n".join([str(i) for i in self.contracts])
