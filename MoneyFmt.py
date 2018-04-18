#!/usr/bin/env python
# encoding: utf-8

class MoneyFmt(object):
    def __init__(self, val):
        self.value = round(float(val), 2)

    def dollarize(self):
        val = self.value
        strvalue = str(val)
        pos = strvalue.find('.')
        while (pos - 3) > 0:
            strvalue = strvalue[:pos - 3] + ',' + strvalue[pos - 3:]
            pos -= 3
        if strvalue.startswith('-'):
            return '-' + '$' + strvalue[1:]
        else:
            return '$' + strvalue

a = MoneyFmt()
a.dollarize(13564161.33)
