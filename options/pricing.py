from enum import Enum
import math
from statistics import NormalDist
import datetime as dt

class PriceModel:
    pass

class BlackScholes(PriceModel):

    def __init__(self, underlying_price: float, strike: float, expiration: float, volatility: float, interest: float):
        self.S = underlying_price
        self.X = strike
        self.t = expiration
        self.sigma = volatility
        self.r = interest
        b = self.r
        self.d1 = (math.log(self.S / self.X)+(b + (self.sigma ** 2) / 2) * self.t)/(self.sigma * (self.t ** .5))
        self.d2 = self.d1 - (self.sigma * (self.t ** .5))
        self.normal = NormalDist(0, 1)

    def call_price(self):
        return self.S * self.normal.cdf(self.d1) - self.X * math.exp(-self.r * self.t) * self.normal.cdf(self.d2)

    def put_price(self):
        return self.X * math.exp(-self.r * self.t) * self.normal.cdf(-self.d2) - self.S * self.normal.cdf(-self.d1) 

    def call_delta(self):
        return self.normal.cdf(self.d1)

    def put_delta(self):
        return self.normal.cdf(self.d1) - 1

    def call_gamma(self):
        return self.normal.pdf(self.d1) / (self.S * self.sigma * (self.t ** .5))

    def put_gamma(self):
        return self.call_gamma()

    def call_theta(self):
        return (-self.X * self.normal.pdf(self.d1) * self.sigma) / (2 * (self.t ** .5)) - self.r * self.X * math.exp(-self.r * self.t) * self.normal.cdf(self.d2)

    def put_theta(self):
        return (-self.X * self.normal.pdf(self.d1) * self.sigma) / (2 * (self.t ** .5)) + self.r * self.X * math.exp(-self.r * self.t) * self.normal.cdf(-self.d2)

    def call_vega(self):
        return self.S * self.normal.pdf(self.d1) * (self.t ** .5)

    def put_vega(self):
        return self.call_vega()

    def call_rho(self):
        return self.t * self.X * math.exp(-self.r * self.t) * self.normal.cdf(self.d2)

    def put_rho(self):
        return -self.t * self.X * math.exp(-self.r * self.t) * self.normal.cdf(-self.d2)

    def call_info(self):
        return {
            "contract_price": self.call_price(), 
            "underlying_price": self.S,
            "expiration": self.t, 
            "volatility": self.sigma, 
            "interest": self.r, 
            "delta": self.call_delta(), 
            "gamma": self.call_gamma(), 
            "theta": self.call_theta(), 
            "vega": self.call_vega(), 
            "rho": self.call_rho(), 
        }

    def put_info(self):
        return {
            "contract_price": self.put_price(), 
            "underlying_price": self.S,
            "expiration": self.t, 
            "volatility": self.sigma, 
            "interest": self.r, 
            "delta": self.put_delta(), 
            "gamma": self.put_gamma(), 
            "theta": self.put_theta(), 
            "vega": self.put_vega(), 
            "rho": self.put_rho(), 
        }
