class Stock:
    def __init__(self, symbol, name, previous_closing_price, current_price):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previous_closing_price
        self.currentPrice = current_price

    def get_change_percent(self):
        percent_change = (((self.previousClosingPrice - self.currentPrice) / self.previousClosingPrice) * 100)
        return percent_change


s1 = Stock('APPL', 'Apple', 450, 435)
print('The', s1.name, 'stock % change from last night was:', str(round(s1.get_change_percent(), 2)) + '%')

s2 = Stock('GLL', 'Google', 850, 835)
print('The', s2.name, 'stock % change from last night was:', str(round(s2.get_change_percent(), 2)) + '%')

