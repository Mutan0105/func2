#!/usr/bin/env python
# encoding: utf-8
import time


def timeit(func, *nkwargs, **kwargs):
    try:
        start = time.clock()
        retval = func(*nkwargs, **kwargs)
        end = time.clock()
        result = (True, retval, end - start)
    except Exception, diag:
        result = (False, str(diag))
    return result


def iteration(n):
    sum = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            sum *= i
    return sum


def mult(x, y):
    return x * y


def myreduce(n):
    return reduce(mult, range(1, n + 1))
    # return reduce(lambda x,y:x*y,range(1,n+1))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def test():
    eachVal = 5
    funcs = (iteration, myreduce, factorial)
    for eachFunc in funcs:
        print '-' * 60
        retval = timeit(eachFunc, eachVal)
        if retval[0]:
            print '%s(%s)=' % (eachFunc.__name__, eachVal), retval[1],
            print 'this func cost %s secs' % retval[2]
        else:
            print '%s(%s)=FAILED: ' % (eachFunc.__name__, eachVal), retval[1]


test()