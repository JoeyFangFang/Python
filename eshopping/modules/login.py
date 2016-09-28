#_*_ coding:utf-8 _*_
'''信用卡登录程序'''

import json

def login(userdbfile):
    #设定计数器
    count = 0
    #设定用户字典，用户锁定字典
    logindb = json.load(open(userdbfile,'r'))  
    while count < 3:
        print "------Please Login:---------"
        name = raw_input("User:")
        password = raw_input("Password:")
        if name not in logindb.keys() or password != logindb[name]["password"] :
            count +=1
            print "用户名/密码错误!你还有{0}次机会".format(3-count)
            continue
        if logindb[name]["locked"] == 'y':
            print "[505]User is Locked. Please phone to 110!"
            continue
        else:
            print "Login Successfully!"
            return name

    else:
        if name in logindb.keys():
            logindb[name]["locked"]='y'
            print "User is Locked. Please phone to 110!"
            json.dump(logindb,open(userdbfile,'w'))
        return False
