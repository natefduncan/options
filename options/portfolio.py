from typing import List
import plotext as plt
import numpy as np

from options.contracts import *
from options.pricing import BlackScholes

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

    def info_graph(self, x_axis: str, y_axis: str):
        input_ranges = {
            "underlying_price": [.01, 100], 
            "expiration": [.01, 2], 
            "volatility": [.01, 1], 
            "interest": [.01, .20], 
        }
        input_defaults = {
            "underlying_price": 50, 
            "expiration": 60/360, 
            "volatility": .50, 
            "interest": .08
        }
        x = np.linspace(input_ranges[x_axis][0], input_ranges[x_axis][1], 50)
        x_outputs = []
        y_outputs = []
        for contract in self.contracts:
            x_output = []
            y_output = []
            for a in x:
                data = {**input_defaults, **{x_axis: a, "strike": contract.strike}}
                bs = BlackScholes(**data)
                if isinstance(contract, Call):
                    info = bs.call_info()
                else:
                    info = bs.put_info()
                x_output.append(info[x_axis] * contract.position)
                y_output.append(info[y_axis] * contract.position)
            x_outputs.append(x_output)
            y_outputs.append(y_output)
        x_sums = [sum(x) for x in zip(*x_outputs)]
        y_sums = [sum(y) for y in zip(*y_outputs)]
        plt.plot(x_sums, y_sums)
        plt.xlabel(x_axis.title().replace("_", " "))
        plt.ylabel(y_axis.title().replace("_", " "))
        plt.title(f"{y_axis.title().replace('_', ' ')} by {x_axis.title().replace('_', ' ')} for {self.name}")
        plt.show()
        #  print(BlackScholes(100, 90, 60/365, .50, .08).call_info())
