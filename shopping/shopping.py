#_*_ coding:utf-8 _*_
#Filename:shopping.py
'''购物中心：
    1. 购物
    2. 查看购物车
    3. 结算
    4. 个人中心
'''
from select import getSelection
from select import getSelection2

shoppinglist = {'PC':5000,
                'Mobile':2300,
                'Mp3':420,
                'SDcard':50,
                'Bike':860
               } 
shoppingCart = {'PC':1,
                'Mobile':2
                }
CreditLine = 20000
Balance = CreditLine

def Buy():
    #购物程序
    print '''--------------显示购物列表-----------'''
    for i,item in enumerate(shoppinglist):
        print '%d \t Goods: %s \t Price: %s'%(i,item,shoppinglist[item])
    print '''-------------------------------'''
    while True:
        ShowCart()
        Dobuy = raw_input('Do you want to buy?(Y/N)')
        if Dobuy =='Y':
            good = getSelection2(shoppinglist)
            appendCart(good) #放入购物车
        else:
            break 
        
def ShowCart():
    print '''--------------显示购物车-----------'''
    for item in shoppingCart:
        print 'Goods: %s \t Acounts: %s'%(item,shoppingCart[item])

def appendCart(select):
    '''放入购物车'''
    item = select[1]
    if item in shoppingCart:
        shoppingCart[item]+=1
    else:
        shoppingCart[item]=1

def Pay():
    '''结算
    '''
    pass
    
def PersonalCenter():
    '''个人中心
    '''
    pass
                      
'''def showBalance():
     print '\t Balance : %s'%balance(shoppingCart)
def balance(shoppingCart = None):
    获取信用卡余额
    balances = CreditLine
    for item in shoppingCart:
        balances = balances - shoppingCart[item]*shoppingDict[item] 
    return balances
'''

def shopping():
    '''购物中心主程序
    '''           
    shoppingMenu = ['Buy','ShowCart','Pay','PersonalCenter','shopBack']
    while True:
        print '''----------购物中心-----------'''
        for i in shoppingMenu:
            print '----%d\t%s-----'%(shoppingMenu.index(i)+1,i)
        print '''---------------------''' 
        choice = getSelection(shoppingMenu)  
        if choice == 1:
            Buy()
        elif choice == 2:
            ShowCart()
        elif choice == 3:
            Pay()
        elif choice == 4:
            PersonalCenter()
            print 'PersonalCenter'
        else:
            print 'shopBack'
            break