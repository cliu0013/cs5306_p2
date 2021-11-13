# import parser
import csv
import pandas as pd
import stock_data
import get_sentiments


POS = 1
NEU = 0
NEG = -1


class Trader:

    def __init__(self, sentiments, prices, cash, shares, daily, direction) -> None:
        self.sentiments = sorted(sentiments.items(), key=lambda x: [0])
        self.prices = prices
        self.cash = cash
        self.shares = shares
        self.daily = daily
        self.direction = direction
        self.records = []
        self.base_shares = self.cash / self.prices["2021-01-28"]

    def buy(self, date):
        if date not in self.prices:
            return
        price = self.prices[date]
        self.cash -= price * self.daily
        self.shares += self.daily
        return

    def sell(self, date):
        if date not in self.prices:
            return
        price = self.prices[date]
        self.cash += price * self.daily
        self.shares -= self.daily
        return

    def getAssets(self, date):
        return self.cash + self.shares * self.prices[date]

    def trade(self):
        for date, sentiment in self.sentiments:
            date = str(date).split()[0]
            if sentiment == POS and self.direction:
                self.buy(date)
            elif sentiment == NEG and self.direction:
                self.sell(date)
            elif sentiment == POS and not self.direction:
                self.sell(date)
            elif sentiment == NEG and not self.direction:
                self.buy(date)

            if date in self.prices:
                self.records.append([date, self.getAssets(
                    date), self.base_shares * self.prices[date]])
            elif self.records:
                self.records.append(
                    [date, self.records[-1][1], self.records[-1][2]])

            # print(date, self.cash, self.shares,
            #       self.records[-1] if self.records else "N/A")

        return


trader = Trader(get_sentiments.getSentiments("s&p"),
                stock_data.getStockData("s&p"), 1_000_000, 0, 3, 1)
trader.trade()

# print(trader.records)


# field names
fields = ['date', 'value']

# data rows of csv file
rows = trader.records

with open('records.csv', 'w') as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(fields)
    write.writerows(rows)


trader = Trader(get_sentiments.getSentiments("gme"),
                stock_data.getStockData("gme"), 1_000_000, 0, 700, 1)
trader.trade()

# print(trader.records)


# field names
fields = ['date', 'value']

# data rows of csv file
rows = trader.records

with open('gme_records.csv', 'w') as f:

    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(fields)
    write.writerows(rows)
