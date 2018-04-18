#!/usr/bin/env python
# encoding: utf-8

class MoneyFmt(object):
    def __init__(self, value=0.0, flag='-'):
        self.mvalue = float(value)
        self.flag = flag

    def dollarize(self):
        val = round(self.mvalue, 2)
        strvalue = str(val)
        pos = strvalue.find('.')
        while (pos - 3) > 0:
            strvalue = strvalue[:pos - 3] + ',' + strvalue[pos - 3:]
            pos -= 3
        if strvalue.startswith('-'):
            print self.flag + '$' + strvalue[1:]
        else:
            print '$' + strvalue

a = MoneyFmt(13564161.33)
a.dollarize()
