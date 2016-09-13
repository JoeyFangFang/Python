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
import json
import time
import re

cardMenu = ['MyCard','Withdraws','Transfers','Repayment','CardLog','Logout']

#cardinfo_dict={
#    '0001':[20000,19000,10000,10000],
#    '0002':[30000,30000,10000,10000],
#    '0003':[10010,10010,10000,10000],
#    }
#readed = json.load(open('cardinfo.txt', 'r'))
#json.dump(readed, open('cardinfo2.txt', 'w'))

def changeCardInfo(userid,changeitem,value=None):
    '''信用卡账户金额相关修改操作
    @param userid:用户名
    @param changeitem:需修改项目，0：信用卡限额，1：当前信用卡可用额度，2：信用卡提现限额，3：当前信用卡可体现额度
    @param value:修改后的值
             所有读取json化操作，相关文件cardinfo.txt    
    '''
    cardid = userid[0]
    cardinfo_dict = json.load(open('cardinfo.txt','r'))
    if value == None:
        return cardinfo_dict[cardid][changeitem]
    cardinfo_dict[cardid][changeitem] = value
    json.dump(cardinfo_dict,open('cardinfo.txt','w'))
    return cardinfo_dict[cardid][changeitem]            
    
def Withdraws(userid):
    user = userid[0]
    cur_credit_limit = changeCardInfo(userid,0)
    cur_credit = changeCardInfo(userid,1)
    cur_withdraws_limit =changeCardInfo(userid,2)
    cur_withdraws = changeCardInfo(userid,3)
    print '''
        用户{0}的信用限额:{1}RMB
        当前可用信用额度:{2}RMB
        提现限额:{3}RMB
        当前可用提现额度:{4}RMB
        '''.format(user,cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws)
    while True:
        money = raw_input('How much do you want to take?(0～{0})'.format(cur_withdraws))
        if re.match(r'\d+',money):
            if 0<=int(money)<=int(cur_withdraws):
                print 'Now you got {0}RMB from creditcard'.format(money)
                new_credit = cur_credit - int(money)
                cur_credit = changeCardInfo(userid,1,new_credit)
                new_withdraws = cur_withdraws - int(money)
                cur_withdraws = changeCardInfo(userid,3,new_withdraws)
                print '''
        \t用户 {0}的信用限额:\t{1}RMB
        \t当前可用信用额度:\t{2}RMB
        \t提现限额:\t{3}RMB
        \t当前可用提现额度:\t{4}RMB
        '''.format(user,cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws)
                while True:
                    decision = raw_input('Do you want to continue to take money?(Y/N)')
                    if decision !='Y'and decision !='N':
                        print 'Please input a valid selection!'
                    else:
                        break
                if decision == 'N':
                    break
            else:
                print 'Please your input is out of limit!'
        else:
            print 'Please input a valid number!'
            
def Repayment(userid):
    user = userid[0]
    cur_credit_limit = changeCardInfo(userid,0)
    cur_credit = changeCardInfo(userid,1)
    cur_withdraws_limit =changeCardInfo(userid,2)
    cur_withdraws = changeCardInfo(userid,3)
    cur_balance = cur_credit_limit - cur_credit
    print '''
        用户{0}的信用限额:{1}RMB
        当前可用信用额度:{2}RMB
        提现限额:{3}RMB
        当前可用提现额度:{4}RMB
        当前应还款额:{5}RMB
        '''.format(user,cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws,cur_balance)
    while True:
        money = raw_input('How much do you want to repay?')
        if re.match(r'\d+',money):
            if int(money)>=0:
                print 'Now you repay {0}RMB from creditcard'.format(money)
                new_credit = cur_credit + int(money)
                cur_credit = changeCardInfo(userid,1,new_credit)
                print new_credit,cur_credit
                time.sleep(15)
                new_withdraws = cur_withdraws + int(money)
                cur_withdraws = changeCardInfo(userid,3,new_withdraws)
                cur_balance = cur_credit_limit - cur_credit
                print '''
        用户{0}的信用限额:\t{1}RMB
        当前可用信用额度:\t{2}RMB
        提现限额:\t{3}RMB
        当前可用提现额度:\t{4}RMB
        当前应还款额:{5}RMB
        '''.format(user,cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws,cur_balance)
                while True:
                    decision = raw_input('Do you want to continue to repay?(Y/N)')
                    if decision !='Y'and decision !='N':
                        print 'Please input a valid selection!'
                    else:
                        break
                if decision == 'N':
                    break
            else:
                print 'Please your input is out of limit!'
        else:
            print 'Please input a valid number!'
                
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
            Withdraws(ID)
        elif choice == 3:
            Transfers()
            print 'Transfers'
        elif choice == 4:
            Repayment(ID)
        elif choice == 5:
            CardLog()
            print 'CardLog'
        else:
            print 'Logout'
            break

def MyCard(userid):
    print '''-----------------我的信用卡-----------'''
    with open('cardinfo.txt','r') as f:
        for line in f:
            userinfo = line.split()
            if userinfo[0] == userid[0]:
                print '''
        用户名：\t{0}
        消费限额：\t{1}
        当前消费额度：\t{2}
        提现限额：\t{3}
        当前提现额度：\t{4}
                '''.format(*userinfo)
                break
                
def Transfers():
    pass
def CardLog():
    pass

creditCardMain()

