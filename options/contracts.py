from enum import IntEnum
import datetime as dt

class Position(IntEnum):
    BUY = 1
    SELL = -1

class Contract:

    def __init__(self, position: Position, price: float, expiration: dt.date, strike: float):
        self.position = position
        self.price = price
        self.expiration = expiration
        self.strike = strike

    def __repr__(self):
        return f"{self.position} {self.expiration} {self.strike} {type(self).__name__} @ ${self.price}"

    def payoff(self, underlying_price: float) -> float:
        return underlying_price 

    def profit(self, underlying_price: float) -> float:
        return underlying_price 

class Call(Contract):

    def payoff(self, underlying_price: float) -> float:
        return max([underlying_price - self.strike, 0]) * self.position

    def profit(self, underlying_price: float) -> float:
        return (self.payoff(underlying_price) - self.price) * self.position

class Put(Contract):

    def payoff(self, underlying_price: float) -> float:
        return max([self.strike - underlying_price, 0]) * self.position

    def profit(self, underlying_price: float) -> float:
        return (self.payoff(underlying_price) - self.price) * self.position
