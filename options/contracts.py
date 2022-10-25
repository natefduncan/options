from enum import Enum
import datetime as dt

class Position(Enum):
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

class Call(Contract):
    pass

class Put(Contract):
    pass
