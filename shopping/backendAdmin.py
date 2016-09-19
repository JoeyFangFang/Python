#_*_ coding:utf-8 _*_
'''后台管理程序:
    1. 创建账户
    2. 锁定账户
    3. 解锁账户
    4. 绑定信用卡
    5. 锁定信用卡
    6. 解锁信用卡
    7. 提升额度
    8. 返回主菜单'''
    
import json

def creatAccount():
    '''创建购物账户并储存在userdb.txt中'''
    useraccounts = json.load(open('userdb.txt','r'))
    print '创建购物账户........'
    while True:
        username = raw_input('Please input the new account name')
        while True:
            userpwd = raw_input("Please input the new account's Password")
            userpwd_ck = raw_input(prompt)
    
    pass

def lockAccount():
    pass

def unlockAccount():
    pass

def bindCreditCard():
    pass

def lockCreditCard():
    pass

def unlockCreditCard():
    pass

def enhanceCreditLimit():
    pass

def adminLogin():
    pass

def adminMain():
    '''后台管理主程序
    '''           
    adminMenu = ['creatAccount','lockAccount','unlockAccount',\
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
    

    