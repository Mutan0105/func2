#!/usr/bin/env python
# encoding: utf-8


class queue(object):
    def __init__(self, list_a):
        self.list_a = list_a

    def enqueue(self, val):
        self.list_a.append(val)
        print self.list_a

    def dequeue(self):
        value = self.list_a.pop(0)
        print '被移除的值为：%s' % value
        print self.list_a


if __name__ == '__main__':
    run = queue([2, 3, 6])
    run.enqueue(1)
    run.dequeue()