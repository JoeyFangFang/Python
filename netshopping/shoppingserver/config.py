#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
'''Configure File'''
import os

#主路径
BASE_DIR = os.path.dirname(__file__)
#数据库路径
DBDIR = BASE_DIR +os.sep+'utility'+os.sep

#Modules路径
ModDir = BASE_DIR +os.sep+'modules'+os.sep

#日志文件路径
Logdir = BASE_DIR + os.sep + 'log' + os.sep


#管理员账户信息
admin = {'AdminName':'admin','AdminPwd':'password'}

'''
    数据库信息：
购物账户信息 shoppingaccounts：
     username(PK) password lockstate bindcard
信用卡账户信息 creditcardaccounts:
     cardaccount(PK) password lockstate
信用卡信息cardinfo: 
    creditaccount(PK) CreditLimit AvailableCredit WithdrawLimit Withdraws
购物车信息CartInfo：
    id(PK) username item qty itemamount
商品信息GoodsInfo: 
    id name price stocks
'''


