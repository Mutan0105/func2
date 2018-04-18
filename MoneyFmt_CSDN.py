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
            return self.flag + '$' + strvalue[1:]
        else:
            return '$' + strvalue

    def update(self, newvalue=None):
        if newvalue is not None:
            self.mvalue = float(newvalue)

    def __nonzero__(self):
        if (self.mvalue == 0):
            return False
        else:
            return True

    def __str__(self):
        return self.dollarize()

    def __repr__(self):
        return repr(self.mvalue)

a = MoneyFmt(13564161.33)
a.dollarize()
