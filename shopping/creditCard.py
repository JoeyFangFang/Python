#_*_ coding:utf-8 _*_
#Filename:creditCard.py
'''信用卡主程序
    1. 我的信用卡
    2. 提现
    3. 转账
    4. 还款
    5. 流水记录
    6. 返回
'''
from login import login
from select import getSelection
from select import getSelection2

cardMenu = ['MyCard','Withdraws','Transfers','Repayment','CardLog','Logout']

def creditCardMain():
    ID = login('carduserdb')
    while True:
        print '''----------信用卡中心-----------'''
        print '用户名：%s'%ID[0]
        for i in cardMenu:
            print '----%d\t%s-----'%(cardMenu.index(i)+1,i)
        print '''---------------------''' 
        choice = getSelection(cardMenu)  
        if choice == 1:
            MyCard(ID)
        elif choice == 2:
            Withdraws()
            print 'Withdraws'
        elif choice == 3:
            Transfers()
            print 'Transfers'
        elif choice == 4:
            Repayment()
            print 'Repayment'
        elif choice == 5:
            CardLog()
            print 'CardLog'
        else:
            print 'Logout'
            break

def MyCard(userid):
    print '''----------我的信用卡-----------'''
    print '用户名：%s'%userid[0]
    with open('cardinfo.txt','r') as f:
        for line in f:
            userinfo = line.split()
            if userinfo[0] == userid[0]:
                print userinfo
                
def Withdraws():
    pass
def Transfers():
    pass
def Repayment():
    pass
def CardLog():
    pass

creditCardMain()

