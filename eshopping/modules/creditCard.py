#_*_ coding:utf-8 _*_
#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
#Filename:creditCard.py
'''信用卡主程序
    1. 我的信用卡    2. 提现    3. 转账    4. 还款    5. 流水记录    6. 返回
'''
from login import login
from select import getSelection
import json,re,time
from eshopping.config.config import CreditCardUsersFile, CardRecordLog,\
    CreditCardAccountFile


#cardinfo_dict={
#    '0001':[20000,19000,10000,10000],
#    '0002':[30000,30000,10000,10000],
#    '0003':[10010,10010,10000,10000],
#    }
#readed = json.load(open('cardinfo.txt', 'r'))
#json.dump(readed, open('cardinfo2.txt', 'w'))

def changeCardInfo(cardid,changeitem,value=None):
    '''信用卡账户金额相关修改操作
    @param cardid:用户名
    @param changeitem:需修改项目，0：信用卡限额，1：当前信用卡可用额度，2：信用卡提现限额，3：当前信用卡可体现额度
    @param value:修改后的值
             所有读取json化操作，相关文件cardinfo.txt    
    '''
    cardinfo_dict = json.load(open(CreditCardUsersFile,'r'))
    if value == None:
        return cardinfo_dict[cardid][changeitem]
    cardinfo_dict[cardid][changeitem] = value
    json.dump(cardinfo_dict,open(CreditCardUsersFile,'w'),sort_keys = True)
    return cardinfo_dict[cardid][changeitem]            
    
def Withdraws(cardid):
    cur_credit_limit = changeCardInfo(cardid,0)
    cur_credit = changeCardInfo(cardid,1)
    cur_withdraws_limit =changeCardInfo(cardid,2)
    cur_withdraws = changeCardInfo(cardid,3)
    print '''
        用户{0}的信用限额:{1}RMB
        当前可用信用额度:{2}RMB
        提现限额:{3}RMB
        当前可用提现额度:{4}RMB
        '''.format(cardid,cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws)
    while True:
        money = raw_input('How much do you want to take?(0～{0})'.format(cur_withdraws))
        if re.match(r'\d+',money):
            if 0<=int(money)<=int(cur_withdraws):
                print 'Now you got {0}RMB from creditcard'.format(money)
                new_credit = cur_credit - int(money)
                cur_credit = changeCardInfo(cardid,1,new_credit)
                new_withdraws = cur_withdraws - int(money)
                cur_withdraws = changeCardInfo(cardid,3,new_withdraws)
                print '''
        \t用户 {0}的信用限额:\t{1}RMB
        \t当前可用信用额度:\t{2}RMB
        \t提现限额:\t{3}RMB
        \t当前可用提现额度:\t{4}RMB
        '''.format(cardid,cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws)
                value = (time.ctime(),cardid,money,)
                record ='时间：%s,用户：%s，操作：提现 %s RMB 成功'%value
                cardRecord(record,value)
                print '*****Log:',record,'******'
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
            
def Repayment(cardid):
    cur_credit_limit = changeCardInfo(cardid,0)
    cur_credit = changeCardInfo(cardid,1)
    cur_withdraws_limit =changeCardInfo(cardid,2)
    cur_withdraws = changeCardInfo(cardid,3)
    cur_balance = cur_credit_limit - cur_credit
    print '''
        用户{0}的信用限额:{1}RMB
        当前可用信用额度:{2}RMB
        提现限额:{3}RMB
        当前可用提现额度:{4}RMB
        当前应还款额:{5}RMB
        '''.format(cardid,cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws,cur_balance)
    while True:
        money = raw_input('How much do you want to repay?')
        if re.match(r'\d+',money):
            if int(money)>=0:
                print 'Now you repay {0}RMB from creditcard'.format(money)
                new_credit = cur_credit + int(money)
                cur_credit = changeCardInfo(cardid,1,new_credit)
                new_withdraws = cur_withdraws + int(money)
                cur_withdraws = changeCardInfo(cardid,3,new_withdraws)
                cur_balance = cur_credit_limit - cur_credit
                print '''
        用户{0}的信用限额:\t{1}RMB
        当前可用信用额度:\t{2}RMB
        提现限额:\t{3}RMB
        当前可用提现额度:\t{4}RMB
        当前应还款额:{5}RMB
        '''.format(cardid,cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws,cur_balance)
                value = (time.ctime(),cardid,money,)
                record ='时间：%s,用户：%s，操作：还款 %s RMB 成功'%value
                cardRecord(record,value)
                print '*****Log:',record,'******'
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
                
def MyCard(cardid):
    CreditCardInfo = json.load(open(CreditCardUsersFile))
    usercardinfo =CreditCardInfo[cardid]
    print '''-----------------我的信用卡-----------'''
    print '''
        用户名：\t{0}
        消费限额：\t{1}
        当前消费额度：\t{2}
        提现限额：\t{3}
        当前提现额度：\t{4}
                '''.format(cardid,*usercardinfo)                
def Transfers():
    pass

def cardRecord(record,value):
    recorddb = json.load(open(CardRecordLog,'r'))
    if not recorddb.has_key(value[1]):
        recorddb[value[1]] = [record,]
    recorddb[value[1]].append(record)
    json.dump(recorddb,open(CardRecordLog,'w'),sort_keys = True)
    

def CardLog(cardid):
    card_logs = json.load(open(CardRecordLog,'r'))
    print '---------用户日志：%s-----------'%cardid
    for item in card_logs[cardid]:
        print item
    raw_input("Press 'ENTER' to back to the Menu")

def creditCardMain():
    cardMenu = ['MyCard','Withdraws','Transfers','Repayment','CardLog','Logout']
    ID = login(CreditCardAccountFile)   #需完善登陆逻辑，登录失败后返回主程序
    while ID:
        print '''----------信用卡中心-----------'''
        print '用户名：%s'%ID
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
            CardLog(ID)
        else:
            print '用户 %s退出，返回主菜单'%ID
            break
    else:
        print '登录失败，返回主菜单'

