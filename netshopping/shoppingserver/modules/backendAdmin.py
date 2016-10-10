#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
'''后台管理程序:
    1. 创建账户    2. 锁定账户    3. 解锁账户
    4. 创建信用卡账户    5. 锁定信用卡    6. 解锁信用卡
    7. 提升额度
    8. 返回主菜单'''

from select import getSelection
from eshopping.config import admin
from eshopping.utility.DBhandle import Select_Item, Insert_Item, Change_Item

def createAccount():
    '''创建购物账户并储存在  shoppingaccounts 中'''
    while True:
        print u'创建购物账户........'
        while True:
            username = raw_input('Please input the new account name--->')
            result = Select_Item('shoppingaccounts', 'username', username)
            if not result:
                break
            print "The new account exits in the db! please try another one"
        while True:
            userpwd = raw_input("Please input the new account's Password--->")
            userpwd_ck = raw_input("Please input the new account's Password Again--->")
            if userpwd == userpwd_ck:
                break
            print "The check user password is not the same as the user password!"   
        useraccount = {'username':username,'password':userpwd,'lockstate':'unlocked'}
        Insert_Item('shoppingaccounts',**useraccount)
        while True:
            choice = raw_input("Do you want to continue to create the user account(Y/N)")
            if choice !="Y" and choice!="N":
                print "Please input the valid selection"
            else:
                break
        if choice == "N":
            break

def lockAccount():
    '''锁定购物账户'''
    username = raw_input("Which account do you want to lock?")
    userinfo = Select_Item('shoppingaccounts', 'username', username)
    if not userinfo:
        print "Please input an exited account!"
    elif userinfo[0][2] =="locked":
        print "The user account %s has been locked!"%username
    else:
        Change_Item('shoppingaccounts', 'username', 'lockstate', ('locked',username))
        print "Now you locked the user account %s"%username
    

def unlockAccount():
    '''解锁购物账户'''
    username = raw_input("Which account do you want to lock?")
    userinfo = Select_Item('shoppingaccounts', 'username', username)
    if not userinfo:
        print "Please input an exited account!"
    elif userinfo[0][2] =="unlocked":
        print "The user account %s has been unlocked!"%username
    else:
        Change_Item('shoppingaccounts', 'username', 'lockstate', ('unlocked',username))
        print "Now you unlocked the user account %s"%username

def createCreditCard():
    '''创建信用卡账户'''
    while True:
        print '创建购物账户........'
        while True:
            cardaccount = raw_input('Please input the new account name--->')
            result = Select_Item('creditcardaccounts', 'cardaccount', cardaccount)
            if not result:
                break
            print "The new account exits in the db! please try another one"
        while True:
            userpwd = raw_input("Please input the new account's Password--->")
            userpwd_ck = raw_input("Please input the new account's Password Again--->")
            if userpwd == userpwd_ck:
                break
            print "The check user password is not the same as the user password!"   
        accountinfo = {'cardaccount':cardaccount,'password':userpwd,'lockstate':'unlocked'}
        Insert_Item('creditcardaccounts',**accountinfo)
        while True:
            choice = raw_input("Do you want to continue to create the user account(Y/N)")
            if choice !="Y" and choice!="N":
                print "Please input the valid selection"
            else:
                break
        if choice == "N":
            break

def lockCreditCard():
    '''锁定信用卡账户'''
    username = raw_input("Which account do you want to lock?")
    userinfo = Select_Item('creditcardaccounts', 'cardaccount', username)
    if not userinfo:
        print "Please input an exited account!"
    elif userinfo[0][2] =="locked":
        print "The user account %s has been locked!"%username
    else:
        Change_Item('creditcardaccounts', 'cardaccount', 'lockstate', ('locked',username))
        print "Now you locked the user account %s"%username

def unlockCreditCard():
    '''解锁信用卡账户'''
    username = raw_input("Which account do you want to lock?")
    userinfo = Select_Item('creditcardaccounts', 'cardaccount', username)
    if not userinfo[0]:
        print "Please input an exited account!"
    elif userinfo[0][2] =="unlocked":
        print "The user account %s has been unlocked!"%username
    else:
        Change_Item('creditcardaccounts', 'cardaccount', 'lockstate', ('unlocked',username))
        print "Now you unlocked the user account %s"%username

def enhanceCreditLimit():
    pass

def adminLogin():
    count = 0
    while count <3:
        inputname = raw_input("Admin Login:--->")
        inputpwd = raw_input("Password:--->")
        if inputname !=admin['AdminName'] or inputpwd != admin['AdminPwd']:
            print "Please input the correct adminaccount and password"
            count +=1
            continue
        print "Admin Login Successful"
        return True
    print "Admin Login Failed"

def adminMain():
    '''后台管理主程序
    '''           
    adminMenu = ['createAccount','lockAccount','unlockAccount',
                 'createCreditCard','lockCreditCard','unlockCreditCard','enhanceCreditLimit']
    if not adminLogin():
        return
    while True:
        print u'''----------后台管理中心-----------'''
        for i in adminMenu:
            print '----%d\t%s-----'%(adminMenu.index(i)+1,i)
        print '''---------------------''' 
        choice = getSelection(adminMenu)  
        if choice == 1:
            createAccount()
        elif choice == 2:
            lockAccount()
        elif choice == 3:
            unlockAccount()
        elif choice == 4:
            createCreditCard()
        elif choice == 5:
            lockCreditCard()
        elif choice == 6:
            unlockCreditCard()
        elif choice == 7:
            enhanceCreditLimit()
        else:
            print '返回主菜单'
            break
    