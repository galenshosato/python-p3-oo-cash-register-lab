#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0, total = 0):
        self.discount = discount
        self.total = total
        self.items = []
        self.last_price = 0
    
    def add_item(self, item, price, quant = 1):
        self.last_price = (price * quant)
        self.total = self.total + self.last_price
        if quant > 1:
            i = quant
            self.last_price = price * quant
            while i > 0:
                (self.items).append(item)
                i -= 1
        else:
            (self.items).append(item)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total - int(self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${self.total}.")
    
    def void_last_transaction(self):
        self.total = self.total - self.last_price
        return self.total





