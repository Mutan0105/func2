#!/usr/bin/env python
# encoding: utf-8

class sq(object):
    def __init__(self,list_a):
        self.list_a = list_a

    def shift(self):
        value = self.list_a.pop(0)
        print '被移除的值为：%s' % value
        print self.list_a

    def unshift(self,val):
        a = []
        a.append(val)
        self.list_a = a + self.list_a
        print self.list_a

    def push(self, val2):
        self.list_a.append(val2)
        print self.list_a

    def pop(self):
        self.list_a.pop(-1)
        print self.list_a


if __name__ == '__main__':
    run = sq([1, 2, 3, 4])
    run.shift()
    run.unshift(7)
    run.push(9)
    run.pop()