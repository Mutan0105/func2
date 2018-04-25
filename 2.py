#!/usr/bin/env python
# encoding: utf-8
class Item(object):
    def __init__(self, product, price):
        self.product = product
        self.price = price

    def __str__(self):
        return '(%s, %.2f)' % (self.product, self.price)


class Cart(object):
    def __init__(self, name):
        self.name = name
        self.cartlist = {}

    def showcart(self):
        for c in self.cartlist:
            print self.name, c, self.cartlist[c]

    def appenditem(self, item, count=1):
        if item not in self.cartlist:
            self.cartlist[item] = count
        else:
            self.cartlist[item] += count

    def deleteitem(self, item, count=1):
        if (item in self.cartlist) and self.cartlist[item] >= count:
            self.cartlist[item] -= count
        if self.cartlist[item] == 0:
            self.cartlist.pop(item)


class User(object):
    def __init__(self, name):
        self.name = name
        self.userdb = []

    def showuser(self):
        print self.name, self.userdb

    def appendcart(self, cart):
        self.userdb.append(cart.name)

    def deletecart(self, cart):
        self.userdb.remove(cart.name)


if __name__ == '__main__':
    i1 = Item('television', 4999)
    i2 = Item('cellphone', 1999)
    print i1, i2
    c1 = Cart('cart1')
    c2 = Cart('cart2')
    c3 = Cart('cart3')
    c1.appenditem(i1, 1)
    c1.appenditem(i2, 1)
    c2.appenditem(i2, 2)
    c3.appenditem(i1, 2)
    c1.showcart()
    c2.showcart()
    c3.showcart()
    u1 = User('Tom')
    u2 = User('Jerry')
    u1.appendcart(c1)
    u2.appendcart(c2)
    u2.appendcart(c3)
    u1.showuser()
    u2.showuser()
