#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年10月5日

@author: Fang
'''
import socket,pickle
from netshopping.shoppingserver.utility.DBhandle import Select_Item
from netshopping.shoppingserver.modules import shopping, creditCard

def handle_request(MsgDict):
    if MsgDict['action'] == 'login':
        retmsg = serverLogin(MsgDict)
        print retmsg
        return serverLogin(MsgDict)
    if MsgDict['action'] == 'ShowGoods':
        return shopping.ShowGoods()
    if MsgDict['action'] =='ShowCart':
        return shopping.ShowCart(MsgDict['username'])
    if MsgDict['action'] =='emptyCart':
        return shopping.emptyCart(MsgDict['username'])
    if MsgDict['action'] =='Buy':
        return shopping.Buy(MsgDict)
    if MsgDict['action'] =='Pay':
        return shopping.Pay(MsgDict['username'])
    
    
    #以下为信用卡中心相关操作函数
    if MsgDict['action'] =='MyCard':
        return creditCard.MyCard(MsgDict['username'])
    if MsgDict['action'] =='Withdraws':
        return creditCard.Withdraws(MsgDict)
    if MsgDict['action'] =='Repayment':
        return creditCard.Repayment(MsgDict)

def serverLogin(MsgDict):
    name = MsgDict['name']
    password = MsgDict['password']
    tablename =MsgDict['tablename']
    option = MsgDict['option']
    returnmsg = {}
    result = Select_Item(tablename,option,name)
    if (not result) or result[0][1] != password:
        returnmsg['result'] = False
        returnmsg['msg'] = u'用户名或密码错误!'
    elif result[0][2] == 'locked':
        returnmsg['result'] = False
        returnmsg['msg'] = u"[505]User is Locked. Please phone to 110!"
    else:
        returnmsg['result'] = True
        returnmsg['msg'] = u'''Login Successfully!        '''
    return returnmsg
    

def mainserver():    
    HOST_PORT = ('127.0.0.1',4001)
    sk= socket.socket()
    sk.bind(HOST_PORT)
    sk.listen(5)
    connection,address = sk.accept()
    print address
    #address is client IP and Port
    revmsg = pickle.loads(connection.recv(1024))
    
    #根据revmsg中action确定调用的操作函数
    sendmsg = pickle.dumps(handle_request(revmsg))

    connection.send(sendmsg)
    connection.close

if __name__ =='__main__':
    while True:
        mainserver()

