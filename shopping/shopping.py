#_*_ coding:utf-8 _*_
#Filename:shopping.py
'''购物中心：
    1. 购物
    2. 清空购物车
    3. 结算
    4. 个人中心
'''
import json
from select import getSelection
from select import getItem
from login import login
from creditCard import changeCardInfo
#from collections import OrderedDict


'''shoppingCart = {'user01':{'PC':1,'Mobile':2},
                'user02':{'SDcard':2,'Bike':1},
                'user03':{'Mp3':2}
                }'''

#json.dump(shoppingCart,open('cartdb.txt','w'),sort_keys = True)



def Buy(userid):
    '''购物程序'''
    goodsDict = json.load(open('goodsdb.txt','r'))
    cartDict = json.load(open('cartdb.txt','r'))
    usercart = cartDict[userid]
    print '''--------------显示商品列表-----------'''
    print '{0:>10}{1:>10}{2:>10}{3:>10}'.format('Item NO.','Item Name','Price','Stock')
    for item in goodsDict:
        print '{0:10}{1:10}{2:10}{3:10}'.format(item,*goodsDict[item])
    print '''-------------------------------'''
    while True:
        print '''--------------显示购物车-----------''' 
        for item in usercart:
            print 'item {0:>10} amount {1:>10} subtotal{2:10}'.format(item,*usercart[item])
        Dobuy = raw_input('Do you want to buy?(Y/N)')
        if Dobuy =='Y':
            good = getItem()
            cartDict[userid] = appendCart(goodsDict[good],usercart) #放入购物车
        else:
            break
    json.dump(cartDict,open('cartdb.txt','w'))
        
def appendCart(select,cart):
    '''放入购物车
    @param select:所选商品对应信息  "Mobile", 2300, 50
    @param cart:购物车信息   "Mp3": [2,840]'''
    itemname = select[0]
    price = select[1]
    if cart.has_key(itemname):
        cart[itemname][0]+=1 #
        cart[itemname][1] = cart[itemname][0]*price        
        print 'add',select,'+1','***','subtotal',cart[itemname][1]
    else:
        cart[itemname] = [1,price]
        print 'new',select,'+1'
    return cart

def emptyCart(userid):
    '''清空购物车'''
    cartDict = json.load(open('cartdb.txt','r'))
    print cartDict[userid]
    select = raw_input('Do you want to EMPTY your cart?(Y/N)?')
    if select =='Y':
        cartDict[userid] = {}
        print 'Your Cart is Empty!'
    json.dump(cartDict,open('cartdb.txt','w'))
                

def Pay(userid):
    '''结算'''
    userbindDict = json.load(open('userbind.txt','r'))
    if userbindDict.has_key(userid):
        carduser = userbindDict[userid]
        availableCredit = changeCardInfo(carduser, 1)
        print availableCredit,'可用额度',carduser,'用户名'
        cartDict = json.load(open('cartdb.txt','r'))
        usercart = cartDict[userid]
        total = 0
        for sub in usercart:
            total += usercart[sub][1]
        if availableCredit>= total:
            changeCardInfo(carduser, 1, availableCredit-total)
            print '购物信息，结算信息'   #待完善
            emptyCart(userid)
        else:
            print "您的信用卡可用额度不足，请提升额度或还款"
    else:
        print '请绑定信用卡'
def PersonalCenter():
    '''个人中心 :绑定信用卡，购物日志'''
    
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

def shoppingMain():
    '''购物中心主程序
    '''           
    shoppingMenu = ['Buy','EmptyCart','Pay','PersonalCenter','shopBack']
    ID = login('shopping_userdb')
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
            print 'shopBack'
            break
    else:
        print '登录错误，返回主菜单'