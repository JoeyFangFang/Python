#_*_ coding:utf-8 _*_
#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
#Filename:creditCard.py
'''信用卡主程序
    1. 我的信用卡    2. 提现    3. 转账    4. 还款    5. 流水记录    6. 返回
'''

from netshopping.shoppingserver.utility.DBhandle import Select_All, Select_Item, Change_Item,Insert_Item, Del_Item
from select import getSelection
import re,time,json
            
def Withdraws(MsgDict):
    ''' 取现'''
    usercreidtinfo = Select_Item('CreditCardInfo', 'creditaccount', MsgDict['username'])[0]
    cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws = usercreidtinfo[1:]
    money = MsgDict['money']
    if re.match(r'\d+',money):
        if 0<=int(money)<=int(cur_withdraws):
            msg = 'Now you got {0}RMB from creditcard'.format(money)
            new_credit = cur_credit - int(money)
            Change_Item('CreditCardInfo', 'creditaccount', 'AvailableCredit', (new_credit,MsgDict['username']))
            new_withdraws = cur_withdraws - int(money)
            Change_Item('CreditCardInfo', 'creditaccount', 'withdraws', (new_withdraws,MsgDict['username']))
#            value = (time.ctime(),MsgDict['username'],money,)
#            record ='时间：%s,用户：%s，操作：提现 %s RMB 成功'%value
#            cardRecord(record,value)
#            print '*****Log:',record,'******'
        else:
            msg = '''Please your input is out of limit! 
                Your current withdraw limit is %d''' %cur_withdraws
    else:
        msg = 'Please input a valid number!'
    return {'msg':msg}
            
def Repayment(MsgDict):
    '''还款 '''
    usercreidtinfo = Select_Item('CreditCardInfo', 'creditaccount', MsgDict['username'])[0]
    cur_credit_limit,cur_credit,cur_withdraws_limit,cur_withdraws = usercreidtinfo[1:]
    cur_balance = cur_credit_limit - cur_credit
    money = MsgDict['money'] 
    if re.match(r'\d+',money):
        if int(money)>=0:
            msg = 'Now you repay {0}RMB from creditcard'.format(money)
            new_credit = cur_credit + int(money)
            Change_Item('CreditCardInfo', 'creditaccount', 'AvailableCredit', (new_credit,MsgDict['username']))
            new_withdraws = cur_withdraws + int(money)
            Change_Item('CreditCardInfo', 'creditaccount', 'withdraws', (new_withdraws,MsgDict['username']))
            cur_balance = cur_credit_limit - cur_credit
#            value = (time.ctime(),MsgDict['username',money,)
#            record ='时间：%s,用户：%s，操作：还款 %s RMB 成功'%value
#            cardRecord(record,value)
#            print '*****Log:',record,'******        
        else:
            msg = 'Please your input is out of limit!'
    else:
        msg = 'Please input a valid number!'
    return {'msg':msg}
            
def MyCard(cardid):
    '''显示信用卡账户信息'''
    cardinfo =Select_Item('CreditCardInfo', 'creditaccount', cardid)[0]
    msg = u'''-----------------我的信用卡-----------
            用户名：\t{0}
            消费限额：\t{1}
            当前消费额度：\t{2}
            提现限额：\t{3}
            当前提现额度：\t{4}
                '''.format(*cardinfo)          
    return {'msg':msg}      

def Transfers():
    pass

def cardRecord(record,value):
    recorddb = json.load(open(Logdir+'CardRecordLog','r'),encoding = 'utf-8')
    if not recorddb.has_key(value[1]):
        recorddb[value[1]] = [record,]
    recorddb[value[1]].append(record)
    json.dump(recorddb,open(Logdir+'CardRecordLog','w'),sort_keys = True)
    

def CardLog(cardid):
    card_logs = json.load(open(Logdir+'CardRecordLog','r'),encoding = 'utf-8')
    print '---------用户日志：%s-----------'%cardid
    for item in card_logs[cardid]:
        print item
    raw_input("Press 'ENTER' to back to the Menu")


