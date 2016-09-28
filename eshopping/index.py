#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang

import sys
from eshopping.config.config import BASE_DIR

sys.path.append(BASE_DIR)

from modules import select,shopping,creditCard,backendAdmin

def main():
    mainList=['Shopping','CreditCard','BackendAdmin']
    while True:
        print '''----------主菜单-----------'''
        for i in mainList:
            print '----%d\t%s-----'%(mainList.index(i)+1,i)
        print '''---------------------''' 
        choice = select.getSelection(mainList)       
        if choice == 1:
            print '进入购物中心........'
            shopping.shoppingMain()
        elif choice == 2:
            print '进入信用卡中心........'
            creditCard.creditCardMain()
        else:
            print '进入后台管理.........'
            backendAdmin.adminMain()
            
if __name__ == '__main__':
    main()