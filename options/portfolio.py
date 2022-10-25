from typing import List
import plotext as plt

from options.contracts import *


class Portfolio:

    def __init__(self, name: str, contracts: List[Contract]):
        self.name = name
        self.contracts = contracts

    def __repr__(self):
        return f"{self.name}:\n" + "\n".join([str(i) for i in self.contracts])

    def parity_graph(self, underlying_max: int):
        underlying = range(0, underlying_max)
        payoff_lists = []
        for contract in self.contracts:
            payoff_lists.append(map(contract.payoff, underlying))
        payoff = [sum(x) for x in zip(*payoff_lists)]
        plt.plot(payoff)
        plt.title(self.name)
        plt.show()
