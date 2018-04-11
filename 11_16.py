#!/usr/bin/env python
# encoding: utf-8
from operator import add, sub, mul, truediv
from random import randint, choice
ops = {'+':add, '-':sub, '*':mul, '/':truediv}
maxtries = 2

def doprob():
    op = choice('+-*/')
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d%s%d = ' % (nums[0], op ,nums[1])
    opps = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if opps == maxtries:
                print 'answer\n%s%d' % (pr,ans)
            else:
                print 'wrong'
                opps += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'try again'
