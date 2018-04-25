#!/usr/bin/env python
# encoding: utf-8
class Item(object):
    #为了每个实例的更改都能被保存，这个地方不能放在初始化里
    db = {'apple':4,'pear':1,'chocolate':3}

    def check(self,name):
        if self.db[name] != 0:
            return True
        else:
            return False

    def delete(self,name):
        if self.check(name) != 0:
            self.db[name] = self.db[name]-1
            return True
        else:
            print name,'already sold out'
            return False

#car中也有一个字典，用来维护每辆车中的物品
class car(object):
    def __init__(self,carname):
        self.carname = carname
        self.car  = {}

    def addthing(self,name):
        it = Item()
        if it.delete(name) == True:
