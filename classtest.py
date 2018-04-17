#!/usr/bin/env python
# encoding: utf-8
class RoundFloatManual(object):
    def __init__(self,val):
        self.value = round (val, 2)

    def __str__(self):
        return '%.2f' % self.value

a = RoundFloatManual(6.33333)
print a