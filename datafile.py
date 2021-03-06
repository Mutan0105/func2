#!/usr/bin/env python
# encoding: utf-8
from datetime import datetime
import shelve, os

class userdatabase(object):
    def __init__(self, dbfile):
        self.db = {}
        if os.path.exists(dbfile):
            self.db = shelve.open(dbfile, 'c')
        self.dbfile = dbfile
        self.flag = False



    def login(self, user, pwd):
        if not self.db.has_key(user):
            self.flag = False
        elif self.db[user][0] == pwd:
            self.db[user][1] = datetime.now()
            self.flag = True

    def deluser(self, user):
        if self.flag:
            self.db.pop(user)
        else:
            print 'login first'

    def updateuser(self, user, pwd):
        if self.flag:
            self.db[user] = [pwd, datetime.now()]
        else:
            print 'login first'

    def listall(self):
        if self.flag:
            for user in self.db:
                print user, self.db[user][0], self.db[user][1]
        else:
            print 'login first'


if __name__ == '__main__':
    user = userdatabase("shelvedata")
    user.login('root', 'root')
    user.updateuser('test1', 'test1')
    user.updateuser('test2', 'test2')
    user.listall()