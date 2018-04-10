#!/usr/bin/python
# -*- encoding: utf-8 -*-
a = [1,5,9,12,5,7]
def add(x, y):
    return x + y

def average():
    b = float(reduce(add,a)) / len(a)
    print b

average()