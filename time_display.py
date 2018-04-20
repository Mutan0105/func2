#!/usr/bin/env python
# encoding: utf-8
import time

class TimeDisplay(object):
    'update()方法可以自由选择系统默认时间或者用户自己给出时间，display()方法可以选择时间显示格式'
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
            time_local = time.strftime('%Y-%m-%d', time.localtime(time_now))#将time模块获取的默认时间转换为年-月-日的格式
            self.year = time_local[0:4]
            self.month = time_local[5:7]
            self.day = time_local[8:]
            # 将上述已经按特点格式转换完毕的系统默认时间，用切片的方法获得年，月，日。赋值后方便在display()方法里将
            # 系统默认或者从用户那里获得的输入用同一种方法进行不同格式输出
    def display(self):
        way = raw_input('采用系统默认默认设置请输入S，自定义请输入SL')
        if way.lower() == 's':
            print '时间为：%s %s, %s' % (self.month,self.day, self.year)#系统默认格式输出
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