#_*_ coding:utf-8 _*_

from select import getSelection
from shopping import shoppingMain
from creditCard import creditCardMain
from backendAdmin import adminMain

def main():
    mainList=['Shopping','CreditCard','BackendAdmin']
    while True:
        print '''----------主菜单-----------'''
        for i in mainList:
            print '----%d\t%s-----'%(mainList.index(i)+1,i)
        print '''---------------------''' 
        choice = getSelection(mainList)       
        if choice == 1:
            print '进入购物中心........'
            shoppingMain()
        elif choice == 2:
            print '进入信用卡中心........'
            creditCardMain()
        else:
            print '进入后台管理.........'
            adminMain()
            
if __name__ == '__main__':
    main()