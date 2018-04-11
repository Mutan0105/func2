#!/usr/bin/env python
# encoding: utf-8
import time
def timeit(func,*nkwargs,**kwargs):
    try:
        t1 = time.clock()
        retval = func(*nkwargs,**kwargs)
        t2 = time.clock()
        result = (True,t2 - t1 ,retval)
    except Exception, diag:
        result =(False ,str(diag))
    return result

def test():
    funcs = (int,long,float)
    vals = (1234, 12.34, '1234')

    for eachFunc in funcs:
        print '_'*20
        for eachVal in vals:
            retval = timeit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) = '% (eachFunc.__name__,'eachVal'), retval[2],'用时%s' % retval[1]
            else:
                print '%s(%s) =Failed: ' % (eachFunc.__name__, 'eachVal'), retval[1]

if __name__=='__main__':
    test()