#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
'''Configure File'''
import os

#主路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#数据库路径
DBDIR =BASE_DIR +os.sep+'database'+os.sep

#数据文件
ShoppingAcountFile = DBDIR+'shopping_userdb.txt'
CreditCardAccountFile = DBDIR+'carduserdb.txt'
CreditCardUsersFile = DBDIR + 'cardinfo.txt'
GoodsDBFile = DBDIR+'goodsdb.txt'
CartDBFile = DBDIR+'cartdb.txt'
UserBindFile = DBDIR +'userbind.txt'
CardRecordLog = DBDIR + 'recordlog.txt'
