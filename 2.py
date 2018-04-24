#!/usr/bin/env python
# encoding: utf-8
class message(object):
   melib = []
    #新生成一条消息,index = 0表示该消息未读
    def makenew(self,me,nameto,namefrom):
        index = 0
        me1 = me+'   from   '+namefrom
        li = [me1,nameto,index]
        self.melib.append(li)

    def checkmessge(self,name):
        for i in self.melib:
            if i[1] == name and i[2] == 0:
                print i[0]
                i[2] = 1

class Room(object):
    #保存参加该房间的用户名称
    namelist = []
    #room message对所有成员可见
    roommessage = []
    def __init__(self,roomname,name1,name2):
        self.roomname = roomname
        self.namelist.append(name1)
        self.namelist.append(name2)

    def addmessage(self,me,name):
        me1 = me + '  from  '+name
        index = 0
        li = [me1,index]
        self.roommessage.append(li)

    def showmessage(self):
        for i in self.roommessage:
            if i[1] == 0:
                print i[0]
                i[1] = 1


class user(object):
    user = []
    roomlist = []

    #用户属性 暂只设置了姓名
    def __init__(self,name):
        self.name = name
        self.user.append(name)

    #用户可以发送信息
    def sendmessage(self,userto):
        if userto in self.user:
            me = raw_input('message:')
            mes = message()
            mes.makenew(me,userto,self.name)
        else:
            print 'no such user'
    #用户可以接收信息
    def accepymessage(self):
        mes = message()
        mes.checkmessge(self.name)

    #创建房间
    def makeroom(self,usname,roomname):
        ro = Room(roomname,usname,self.name)
        self.roomlist.append(ro)

    #向房间中发信息
    def talkroom(self,roomname,mes):
        for i in self.roomlist:
            if i.roomname == roomname:
                i.addmessage(mes,self.name)

    #接收房间中的信息
    def showroommessage(self,roomname):
        for i in self.roomlist:
            if i.roomname == roomname:
                i.showmessage()

if __name__ == '__main__':
    u1 = user('A')
    u2 = user('B')
    u3 = user('C')
    u1.makeroom('B','room1')
    u1.talkroom('room1','hello B')
    u1.makeroom('C','room2')
    u1.talkroom('room2','hello C')
    u2.showroommessage('room1')
    u3.showroommessage('room2')
    u2.talkroom('room1','this is B')
    u1.showroommessage('room1')
    u1.showroommessage('room2')