#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
'''后台管理程序:
    1. 创建账户    2. 锁定账户    3. 解锁账户
    4. 绑定信用卡    5. 锁定信用卡    6. 解锁信用卡
    7. 提升额度
    8. 返回主菜单'''
    
import json
from select import getSelection
from eshopping.config.config import ShoppingAcountFile, CreditCardAccountFile

def creatAccount():
    '''创建购物账户并储存在shopping_userdb.txt中'''
    useraccounts = json.load(open(ShoppingAcountFile,'r'))
    print '创建购物账户........'
    while True:
        username = raw_input('Please input the new account name')
        if username in useraccounts:
            print "The new account exits in the db! please try another one"
            continue
        while True:
            userpwd = raw_input("Please input the new account's Password")
            userpwd_ck = raw_input("Please input the new account's Password Again")
            if userpwd == userpwd_ck:
                break
            print "The check user password is not the same as the user password!"   
        useraccounts[username] = {'password':userpwd,'locked':'n'}
        while True:
            choice = raw_input("Do you want to continue to create the user account(Y/N)")
            if choice !="Y" and choice!="N":
                print "Please input the valid selection"
            else:
                break
        if choice == "N":
            json.dump(useraccounts,open(ShoppingAcountFile,'w'))
            break

def lockAccount():
    '''锁定购物账户'''
    useraccounts = json.load(open(ShoppingAcountFile,'r'))
    while True:
        username = raw_input("Which account do you want to lock?")
        if username not in useraccounts:
            print "Please input an exited account!"
            continue
        elif useraccounts[username]["locked"] =="y":
            print "The user account %s has been locked!"%username
        else:
            useraccounts[username]["locked"] = "y"
            print "Now you locked the user account %s"%username
        json.dump(useraccounts,open(ShoppingAcountFile,'w'))
        break
    

def unlockAccount():
    '''解锁购物账户'''
    useraccounts = json.load(open(ShoppingAcountFile,'r'))
    while True:
        username = raw_input("Which account do you want to unlock?")
        if username not in useraccounts:
            print "Please input an exited account!"
            continue
        elif useraccounts[username]["locked"] =="n":
            print "The user account %s has not been locked!"%username
        else:
            useraccounts[username]["locked"] = "n"
            print "Now you unlocked the user account %s"%username
        json.dump(useraccounts,open(ShoppingAcountFile,'w'))
        break

def bindCreditCard():
    pass

def lockCreditCard():
    '''锁定信用卡账户'''
    carduserdb = json.load(open(CreditCardAccountFile,'r'))
    while True:
        account = raw_input("Which credit account do you want to lock?")
        if account not in carduserdb:
            print "Please input an exited account!"
            continue
        elif carduserdb[account]["locked"] =="y":
            print "The user account %s has been locked!"%account
        else:
            carduserdb[account]["locked"] = "y"
            print "Now you locked the user account %s"%account
        json.dump(carduserdb,open(CreditCardAccountFile,'w'))
        break

def unlockCreditCard():
    '''解锁信用卡账户'''
    carduserdb = json.load(open(CreditCardAccountFile,'r'))
    while True:
        account = raw_input("Which credit account do you want to unlock?")
        if account not in carduserdb:
            print "Please input an exited account!"
            continue
        elif carduserdb[account]["locked"] =="n":
            print "The user account %s has been unlocked!"%account
        else:
            carduserdb[account]["locked"] = "n"
            print "Now you unlocked the user account %s"%account
        json.dump(carduserdb,open(CreditCardAccountFile,'w'))
        break

def enhanceCreditLimit():
    pass

def adminLogin():
    adminname = 'administrator'
    adminpwd ='123123'
    count = 0
    while count <3:
        inputname = raw_input("Admin Login:")
        inputpwd = raw_input("Password")
        if inputname !=adminname or inputpwd != adminpwd:
            print "Please input the correct adminaccount and password"
            count +=1
            continue
        print "Admin Login Successful"
        return True
    print "Admin Login Failed"
    return False

def adminMain():
    '''后台管理主程序
    '''           
    adminMenu = ['creatAccount','lockAccount','unlockAccount',
                 'bindCreditCard','lockCreditCard','unlockCreditCard','enhanceCreditLimit']
    if not adminLogin():
        return
    while True:
        print '''----------后台管理中心-----------'''
        for i in adminMenu:
            print '----%d\t%s-----'%(adminMenu.index(i)+1,i)
        print '''---------------------''' 
        choice = getSelection(adminMenu)  
        if choice == 1:
            creatAccount()
        elif choice == 2:
            lockAccount()
        elif choice == 3:
            unlockAccount()
        elif choice == 4:
            bindCreditCard()
        elif choice == 5:
            lockCreditCard()
        elif choice == 6:
            unlockCreditCard()
        elif choice == 7:
            enhanceCreditLimit()
        else:
            print '返回主菜单'
            break

    