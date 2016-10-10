#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang

import pickle,socket
from netshopping.shoppingserver.modules.select import getSelection

def interactiveMsg(MsgDict):
    '''与服务器信息交互'''
    pkMsg = pickle.dumps(MsgDict)
    ServerIP_PORT = ('127.0.0.1',4001)   #define SERVER's IP and PORT
    sk = socket.socket()
    sk.connect(ServerIP_PORT)
    sk.send(pkMsg)
    getmsg = sk.recv(1024)
    while True:
        buf = sk.recv(1024)
        if not len(buf):
            break
        else:
            getmsg = getmsg + buf
    sk.close() 
    return pickle.loads(getmsg)

def clientLogin(tablename,option):
    '定义客户端登录程序'
    count = 0
    while count<3:
        name = raw_input('Shopping UserName is--->')
        password = raw_input("Password--->")
        sendmsg ={'action':'login',
                  'name':name,
                  'password':password,
                  'tablename':tablename,
                  'option':option
                  }
        recvmsg = interactiveMsg(sendmsg)
        if recvmsg['result'] == False:
            print recvmsg['msg']
            count +=1
        else:
            print recvmsg['msg']
            return name

def actionFunc(action,username):
    '''传递参数至服务器端，调用相应函数'''
    MsgDict= {'action':action,'username':username}
    if action =='Buy':
        Dobuy = raw_input('Do you want to buy?(Y/N)')
        if Dobuy =='Y':
            selection = raw_input('Please input the Item Number what do you want to buy?')
            MsgDict['ItemNo'] = selection
        else:
            return {'msg':'back.....'}
    if action == 'Withdraws':
        money = raw_input('How much do you want to take?')
        MsgDict['money'] = money
    if action == 'Repayment':
        money = raw_input('How much do you want to repay?')
        MsgDict['money'] = money
    return interactiveMsg(MsgDict)        

def shoppingMain():
    '''购物中心主程序    '''           
    shoppingMenu = ['ShowGoods','ShowCart','Buy','EmptyCart','Pay','PersonalCenter','ShopBack']
    ID = clientLogin('shoppingaccounts','username')
    while ID:
        print u'''----------购物中心-----------'''
        for i in shoppingMenu:
            print '----%d\t%s-----'%(shoppingMenu.index(i)+1,i)
        print '''---------------------''' 
        choice = getSelection(shoppingMenu)
        action = shoppingMenu[choice-1]
        if choice in range(1,7):
            actionresult = actionFunc(action,ID)
            print actionresult['msg']  
        else:
            print 'ShopBack'
            break
    else:
        print u'登录错误，返回主菜单'



def creditCardMain():
    cardMenu = ['MyCard','Withdraws','Transfers','Repayment','CardLog','Logout']
    ID = clientLogin('creditcardaccounts','cardaccount')   #需完善登陆逻辑，登录失败后返回主程序
    while ID:
        print u'''----------信用卡中心-----------'''
        print u'用户名：%s'%ID
        for i in cardMenu:
            print '----%d\t%s-----'%(cardMenu.index(i)+1,i)
        print '''---------------------''' 
        choice = getSelection(cardMenu)  
        action = cardMenu[choice-1]
        if choice in range(1,6):
            actionresult = actionFunc(action,ID)
            print actionresult['msg']  
        else:
            print '用户 %s退出，返回主菜单'%ID
            break
    else:
        print '登录失败，返回主菜单'

def adminMain():
    pass