#!/usr/bin/env python
# encoding: utf-8
import math
class line(object):
    '根据两组坐标定义直线'
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        zb = (self.a, self.b)
        return str(zb)
    __repr__ = __str__

    def lenth(self):
        self.lenth = math.sqrt((self.a[0] - self.b[0])**2 + (self.a[1] - self.b[1])**2)
        print self.lenth

    def slope(self):
        if self.a[1] == self.b[1]:
            print '直线斜率为0'
        else:
            self.slope = float((self.a[0] - self.b[0])) / (self.a[1] - self.b[1])
            print self.slope


if __name__ == '__main__':
    run = line((4,2),(2,2))
    print run
    run.lenth()
    run.slope()