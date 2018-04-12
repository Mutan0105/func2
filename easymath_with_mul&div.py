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
    if op == '/':
        nums = [float(x) for x in nums]#转换为float保证结果为浮点数
        ans = round(ops[op](*nums),2) #除法运算保留2位小数
    else:
        ans = ops[op](*nums)
    pr = '%d%s%d = ' % (nums[0], op ,nums[1])
    opps = 0
    while True:
        try:
            if float(raw_input(pr)) == float(ans): #使用float而不是int是为了保证除法运算能够输入小数，保证结果正确
                print 'correct'
                break
            if opps == maxtries:
                print 'answer\n%s%d' % (pr,ans)
            else:
                print 'wrong'
                opps += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'try again'

def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again?[Y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()
