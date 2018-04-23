#!/usr/bin/env python
# encoding: utf-8
class stack(object):
    def __init__(self,list_a):
        self.list_a = list_a

    def push(self,val):
        self.list_a.append(val)
        print self.list_a

    def pop(self,val2):
        self.list_a.remove(val2)
        print self.list_a

    def isempty(self):
        flag = len(self.list_a)
        if flag == 0:
            print 0
        else:
            print 1


if __name__ == '__main__':
    run = stack([1,3])
    run.push(7)
    run.push(2)
    run.pop(2)
    run.isempty()
