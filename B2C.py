#!/usr/bin/env python
# encoding: utf-8


class customer(object):
    def __init__(self):
        pass


class item(object):
    "modify可以修改库存量，直接使用字典方法进行"
    db = {'apple': 0, 'banana': 0, 'milk': 0}

    def modify(self):
        flag = True
        while flag:
            name = raw_input('需要修改的库存项目名称，若不存在将自动创建此项，结束修改请输入done。')
            number = int(raw_input('更新该项目的存量'))
            if name == 'done':
                flag = False
                break
            else:
                self.db[name] = number

    def showstock(self):
        print self.db

class cart(object):
    def __init__(self, name):
        self.Cartname = name
        self.cart = []

    def CreatCart(self):
        self.cart.append(self.Cartname)
        print self.cart

    def DelCart(self, cartname):
        self.cart.remove(cartname)
        print self.cart

    def ModifyCart(self, cartname2):
        which_item = raw_input('商品名称')
        number = int(raw_input('数量'))
        i = item()
        if self.db[which_item] < number:
            print '商品数量不够'
        else:
            self.db[which_item] = number
            self.Cartname = self.db
        print self.cart
        print self.db


if __name__ == '__main__':
    a = item()
    a.showstock()
    a.modify()
    a.showstock()

    run = cart('a')
    run.CreatCart()
    run.ModifyCart('a')