#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
#Filename:shopping.py

from netshopping.shoppingserver.utility.DBhandle import Select_All, Select_Item, Change_Item,Insert_Item, Del_Item
from login import login
from select import getSelection
'''购物中心：
    1. 购物    2. 清空购物车    3. 结算    4. 个人中心
'''

def ShowGoods():
    '''显示购物商城商品'''
    goodslist = Select_All('GoodsInfo')
    msg = u'''--------------显示商品列表-----------
        {0:>10}{1:>10}{2:>10}{3:>10}\n'''.format('Item NO.','Item Name','Price','Stock')
    for item in goodslist:
        msg += '{0:10}{1:10}{2:10}{3:10}\n'.format(*item)
    return {'msg':msg,}

def ShowCart(userid):
    '''显示userid的购物车'''
    usercart = Select_Item('CartInfo', 'username',userid)
    msg = u'''--------------显示购物车----------- 
         {0:>10}{1:>10}{2:>10}{3:>10}{4:>10}\n'''.format('Id.','User Name','Item','QTy','Amount')
    for item in usercart:
        msg += '{0:>10}{1:>10}{2:>10}{3:>10}{4:>10}\n'.format(*item)
    return {'msg':msg,}

def Buy(MsgDict):
    '''购物程序'''
    good = Select_Item('GoodsInfo', 'id', MsgDict['ItemNo'])
    if not good:
        return {'msg':'Please input the correct Item Number!',}
    usercart = Select_Item('CartInfo', 'username',MsgDict['username'])
    itemname,price = str(good[0][1]),good[0][2]
    found = False
    for item in usercart:
        if itemname == str(item[2]):
            itemid = item[0]
            newQty = item[3]+1
            newAmount = item[4]+price
            Change_Item('CartInfo','id', 'Qty', (newQty,itemid))
            Change_Item('CartInfo','id', 'itemAmount', (newAmount,itemid))
            found = True
            break
    if not found:
        itemdetail ={'username':MsgDict['username'],
                'item':itemname,
                'Qty':1,
                'itemamount':price}
        Insert_Item('CartInfo',**itemdetail)
    return {'msg':'do Buy!',}
        
def emptyCart(userid):
    '''清空购物车'''
    Del_Item('CartInfo', 'username', userid)
    return {'msg':'Your Cart is Empty!',}
                

def Pay(userid):
    '''结算'''
    shoppinguser = Select_Item('ShoppingAccounts', 'username', userid)[0]
    account = str(shoppinguser[3])
    if account:
        usercart = Select_Item('CartInfo', 'username',userid)   #获取购物车信息
        total = 0
        for item in usercart:           #获取总计
            itemamount = item[4]
            total +=itemamount
        usercard = Select_Item('CreditCardInfo', 'creditaccount', account)[0]
        print usercard
        CreditLimit,AvailableCredit,WithdrawLimit,Withdraws = usercard[1:]
        if AvailableCredit>= total:
            AvailableCredit = AvailableCredit -total
            Change_Item('CreditCardInfo', 'creditaccount', 'AvailableCredit', (AvailableCredit,account))
            msg = u'购物信息，结算信息'   #待完善
            msg += emptyCart(userid)['msg']
        else:
            msg = "您的信用卡可用额度不足，请提升额度或还款"
    else:
        msg = '请绑定信用卡'
    return {'msg':msg,}

def PersonalCenter(userid):
    '''个人中心 :绑定信用卡，购物日志'''
    personcenterMenu = ['BindCard','ShoppingLog','Return']
    print '''----------个人中心-----------'''
    for i in personcenterMenu:
        print '----%d\t%s-----'%(personcenterMenu.index(i)+1,i)
    print '''---------------------''' 
    choice = getSelection(personcenterMenu)  
    if choice == 1:
        BindCard(userid)
    elif choice == 2:
        ShoppingLog(userid)
    else:
        print 'Return'
        
def BindCard(userid):
    '''绑定信用卡用户carduserdb到购物账户shopping_userdb；生成userbind关联文件
    '''
    userdetail = Select_Item('ShoppingAccounts', 'username', userid)[0]
    account = userdetail[3]
    if account:
        print 'You have bound your shoppingaccount {0} to creditcard {1}'.format(userid,account)
        while True:
            choice = raw_input('Do you want change binding?(Y/N)')
            if choice != 'N' and choice !='Y':
                print 'Please do  a vilid selection!'
                continue
            elif choice =='N':
                return account
            else:
                break
    print '---Login the creditcard account you want to bind---'  
    cardaccount = login('CreditCardAccounts','cardaccount')
    if cardaccount:
        Change_Item('ShoppingAccounts', 'username', 'bindcard', (cardaccount,userid))
        print 'You bound your shoppingaccount {0} to creditcard {1} successfully'.format(userid,cardaccount)
        return cardaccount
    else:
        print ' shopping account Logon Failed!'
        
    
def ShoppingLog(cardid):
    pass                 


       
        