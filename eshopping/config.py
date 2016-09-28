#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
'''Configure File'''
import os

#主路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#数据库路径
DBDIR =BASE_DIR +os.sep+'database'+os.sep
'''
数据库信息：
购物账户信息shoppingaccounts： username password lockstate bindcaard
信用卡账户信息creditcardaccounts: id password lockstate
信用卡信息cardinfo: id CreditLimit AvailableCredit WithdrawLimit Withdraws
购物车信息CartInfo：username item qty
商品信息GoodsInfo: id name price stocks
'''



'''数据文件
ShoppingAcountFile = DBDIR+'shopping_userdb.txt'
CreditCardAccountFile = DBDIR+'carduserdb.txt'
CreditCardUsersFile = DBDIR + 'cardinfo.txt'
GoodsDBFile = DBDIR+'goodsdb.txt'
CartDBFile = DBDIR+'cartdb.txt'
UserBindFile = DBDIR +'userbind.txt'
CardRecordLog = DBDIR + 'recordlog.txt'
'''