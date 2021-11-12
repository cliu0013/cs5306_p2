# import parser
import pandas as pd
import stock_data

POS = 1
NEU = 0
NEG = -1


class Trader:

    def __init__(self, sentiments, prices, cash, shares, daily, direction) -> None:
        self.sentiments = sentiments
        self.prices = prices
        self.cash = cash
        self.shares = shares
        self.daily = daily
        self.direction = direction

    def hasNext(self):
        return

    def next(self):
        return

    def buy(self):
        return

    def sell(self):
        return

    def trade(self):
        while self.hasNext():
            sentiment = self.next()
            if sentiment == POS and self.direction:
                self.buy()
                pass
            if sentiment == NEG and self.direction:
                self.sell()
                pass
            if sentiment == POS and not self.direction:
                self.sell()
                pass
            if sentiment == NEG and not self.direction:
                self.buy()
                pass

        return


trader = Trader(0, 0, 0, 0, 0)
