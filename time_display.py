#!/usr/bin/env python
# encoding: utf-8
import time

class TimeDisplay(object):
    def __init__(self):
        pass
    def update(self):
        system = raw_input('采用系统默认时间输入S，自定义请输入SL')
        if system.lower() == 'sl':
            self.year = raw_input('输入年份')
            self.month = raw_input('输入月份')
            self.day = raw_input('输入日期')

        else:
            time_now = int(time.time())
            self.time_local = time.localtime(time_now)

    def display(self):
        way = raw_input('采用系统默认默认设置请输入S，自定义请输入SL')
        if way.lower() == 's':
            print time.strftime('%Y-%m-%d', self.time_local)
        else:
            print "输入'MDY'来按照 MM/DD/YY来显示\n输入'MDYY'来按照 MM/DD/YYYY来显示\n" \
                  "输入'DMY'来按照 DD/MM/YYYY来显示\n输入'DMYY'来按照 DD/MM/YYYY来显示"
            which_display = raw_input('请选择显示格式：')
            if which_display == 'MDY':
                print '时间为：%s/%s/%s' % (self.month,self.day, self.year[2:])
            elif which_display == 'MDYY':
                print '时间为：%s/%s/%s' % (self.month, self.day, self.year)
            elif which_display == 'DMY':
                print '时间为：%s/%s/%s' % (self.day, self.month, self.year[2:])
            elif which_display == 'DMYY':
                print '时间为：%s/%s/%s' % (self.day, self.month, self.year)

if __name__ == '__main__':
    run = TimeDisplay()
    run.update()
    run.display()