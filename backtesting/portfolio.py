# backtesting/portfolio.py

class Portfolio:
    def __init__(self, initial_capital=100000):
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.positions = {}
        self.history = []

    def buy(self, symbol, price, quantity):
        cost = price * quantity
        if self.cash >= cost:
            self.cash -= cost
            self.positions[symbol] = self.positions.get(symbol, 0) + quantity
            self.history.append((symbol, 'BUY', price, quantity, self.cash))
        else:
            print(f"Insufficient cash to buy {symbol}")

    def sell(self, symbol, price, quantity):
        if symbol in self.positions and self.positions[symbol] >= quantity:
            self.positions[symbol] -= quantity
            proceeds = price * quantity
            self.cash += proceeds
            self.history.append((symbol, 'SELL', price, quantity, self.cash))
        else:
            print(f"Not enough holdings to sell {symbol}")

    def get_total_value(self, current_prices):
        value = self.cash
        for symbol, qty in self.positions.items():
            value += qty * current_prices.get(symbol, 0)
        return value

    def get_history(self):
        return self.history