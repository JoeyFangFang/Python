#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
#Filename:shopping.py
from eshopping.utility.DBhandle import Select_All, Select_Item, Change_Item,\
    Insert_Item, Del_Item
from login import login
from select import getSelection
'''购物中心：
    1. 购物    2. 清空购物车    3. 结算    4. 个人中心
    
'''

def ShowGoods():
    goodslist = Select_All('GoodsInfo')
    print '''--------------显示商品列表-----------'''
    print '{0:>10}{1:>10}{2:>10}{3:>10}'.format('Item NO.','Item Name','Price','Stock')
    for item in goodslist:
        print '{0:10}{1:10}{2:10}{3:10}'.format(*item)
    print '''-------------------------------'''

def getItem():
    '''购物商品选择'''
    while True:
        ShowGoods()
        selection = raw_input('Please input the Item Number what do you want to buy?')
        result = Select_Item('GoodsInfo', 'id', selection)
        if not result:
            print 'Please input the correct Item Number!'
        else:
            return result[0]

def Buy(userid):
    '''购物程序'''
    while True:
        usercart = Select_Item('CartInfo', 'username',userid)
        print '''--------------显示购物车-----------''' 
        print '{0:>10}{1:>10}{2:>10}{3:>10}{4:>10}'.format('Id.','User Name','Item','QTy','Amount')
        for item in usercart:
            print '{0:>10}{1:>10}{2:>10}{3:>10}{4:>10}'.format(*item)
        Dobuy = raw_input('Do you want to buy?(Y/N)')
        if Dobuy =='Y':
            good = getItem()
            itemname,price = str(good[1]),good[2]
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
                itemdetail ={'username':userid,
                        'item':itemname,
                        'Qty':1,
                        'itemamount':price}
                Insert_Item('CartInfo',**itemdetail)
        else:
            break
        
def emptyCart(userid):
    '''清空购物车'''
    usercart = Select_Item('CartInfo', 'username',userid)
    print '''--------------显示购物车-----------''' 
    print '{0:>10}{1:>10}{2:>10}{3:>10}{4:>10}'.format('Id.','User Name','Item','QTy','Amount')
    for item in usercart:
        print '{0:>10}{1:>10}{2:>10}{3:>10}{4:>10}'.format(*item)
    select = raw_input('Do you want to EMPTY your cart?(Y/N)?')
    if select =='Y':
        Del_Item('CartInfo', 'username', userid)
        print 'Your Cart is Empty!'
                

def Pay(userid):
    '''结算'''
    shoppinguser = Select_Item('ShoppingAccounts', 'username', userid)[0]
    print shoppinguser
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
        print CreditLimit,AvailableCredit,WithdrawLimit,Withdraws
        if AvailableCredit>= total:
            AvailableCredit = AvailableCredit -total
            Change_Item('CreditCardInfo', 'creditaccount', 'AvailableCredit', (AvailableCredit,account))
            print '购物信息，结算信息'   #待完善
            emptyCart(userid)
        else:
            print "您的信用卡可用额度不足，请提升额度或还款"
    else:
        print '请绑定信用卡'
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

def shoppingMain():
    '''购物中心主程序
    '''           
    shoppingMenu = ['Buy','EmptyCart','Pay','PersonalCenter','ShopBack']
    ID = login('ShoppingAccounts','username')
    while ID:
        print '''----------购物中心-----------'''
        for i in shoppingMenu:
            print '----%d\t%s-----'%(shoppingMenu.index(i)+1,i)
        print '''---------------------''' 

        choice = getSelection(shoppingMenu)  
        if choice == 1:
            Buy(ID)
        elif choice == 2:
            emptyCart(ID)
        elif choice == 3:
            Pay(ID)
        elif choice == 4:
            PersonalCenter(ID)
            print 'PersonalCenter'
        else:
            print 'ShopBack'
            break
    else:
        print '登录错误，返回主菜单'
        
       
        