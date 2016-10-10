#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2016年10月5日

@author: Fang
'''
from netshopping.shoppingclient import modules

    
def main():
    mainList=['Shopping','CreditCard','BackendAdmin']
    while True:
        print u'''----------主菜单-----------'''
        for i in mainList:
            print '----%d\t%s-----'%(mainList.index(i)+1,i)
        print '''---------------------''' 
        choice = modules.getSelection(mainList)       
        if choice == 1:
            print u'进入购物中心........'
            modules.shoppingMain()
        elif choice == 2:
            print u'进入信用卡中心........'
            modules.creditCardMain()
        else:
            print u'进入后台管理.........'
            modules.adminMain()
            
if __name__ =='__main__':
    main()


