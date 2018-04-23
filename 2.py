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

            if self.car.has_key(name) == True:
                self.car[name] = self.car[name]+1
            else:
                self.car[name] = 1


    def showthings(self):
        for i in self.car:
            print i,self.car[i]

#用户用一个list来存储生成的car对象，之后就用list下标就可以访问到实例
class user(object):
    def __init__(self):
        self.index = 0
        self.carlist = []

    def addcar(self,carname):
        ca = car(carname)
        self.carlist.append(ca)

    def showcar(self):
        for i in self.carlist:
            print i.carname

    def addthing(self,name,carname):
        for i in self.carlist:
            if i.carname == carname:
                i.addthing(name)

    def showthing(self):
        for i in self.carlist:
            print i.carname,'has things:'
            i.showthings()


#调用的逻辑 我做的是用户调用车，车在添加物品是调用物体库
if __name__ =='__main__':
    us = user()
    us.addcar('car1')
    us.addcar('car2')
    us.addthing('pear', 'car1')
    us.addthing('pear', 'car2')
    # us.addthing('chocolate', 'car1')
    us.addthing('pear', 'car2')
    us.showthing()