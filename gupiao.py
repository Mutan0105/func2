#!/usr/bin/env python
# encoding: utf-8

class datafile(object):
    def __init__(self, name, stock_symbol, buytime, price, quantity):
        self.name = name
        self.stock_symbol = stock_symbol
        self.buytime = buytime
        self.price = float(price)
        self.quantity = float(quantity)

    def __str__(self):
        return '%s %s %s %.2f %d' % (self.name, self.stock_symbol, self.buytime, self.price, self.quantity)


    def AddNewStock(self):
        self.stockdetail = [self.name, self.stock_symbol, self.buytime, self.price, self.quantity]
        self.stocklist = {self.name: self.stockdetail}
