#_*_ coding:utf-8 _*_
'''信用卡登录程序'''

from eshopping.utility.DBhandle import Select_Item,Change_Item


def login(accountdb,option):
    '''
    @param accountdb:登录用户数据库
    @param option：用户字段名 
    '''
    #设定计数器
    count = 0
    while count < 3:
        print "------Please Login:---------"
        name = raw_input("User:")
        password = raw_input("Password:")
        result = Select_Item(accountdb,option,name)[0]
        if (not result) or result[1] != password:
            count +=1
            print "用户名或密码错误!你还有{0}次机会".format(3-count)
            continue
        if result[2] == 'locked':
            print "[505]User is Locked. Please phone to 110!"
            continue
        else:
            print "Login Successfully!"
            return name

    else:
        if result:
            v = 'locked',name
            Change_Item(accountdb, option, 'lockstate', v)
            print "User is Locked. Please phone to 110!"
    
