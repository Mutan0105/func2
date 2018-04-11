#!/usr/bin/env python
# encoding: utf-8
import os
def creat(filename):
    newfile = raw_input('输入文件名：')
    with open(filename,'r') as f:
        doneline = map(lambda line:line.strip() ,f)
    with open(newfile,'w') as dfile:
        for lines in doneline:
            dfile.write(lines)
            dfile.write(os.linesep)


creat('11_11_text.txt')