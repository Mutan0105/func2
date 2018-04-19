#!/usr/bin/env python
# encoding: utf-8
import time

class TimeDisplay(object):
    def __init__(self):

    def update():
        system = raw_input('采用系统默认时间输入S，自定义请输入SL')
        if system.lower() == 'sl':
            year = int(raw_input('输入年份'))
            month = int(raw_input('输入月份'))
            day = int(raw_input('输入日期'))
            time_local =
        else:
            time_now = int(time.time())
            time_local = time.localtime(time_now)

    def display():
        way = raw_input('采用系统默认默认设置请输入S，自定义请输入SL')
        if way.lower() ==