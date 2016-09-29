#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
'''Configure File'''
import os

#主路径
BASE_DIR = os.path.dirname(__file__)
#数据库路径
DBDIR =BASE_DIR +os.sep+'utility'+os.sep
'''
    数据库信息：
购物账户信息shoppingaccounts：
     username(PK) password lockstate bindcard
信用卡账户信息creditcardaccounts:
     creditaccount(PK) password lockstate
信用卡信息cardinfo: 
    creditaccount(PK) CreditLimit AvailableCredit WithdrawLimit Withdraws
购物车信息CartInfo：
    id(PK) username item qty itemamount
商品信息GoodsInfo: 
    id name price stocks
'''


