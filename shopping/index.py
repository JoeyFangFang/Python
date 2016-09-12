#_*_ coding:utf-8 _*_

from shopping import shopping
from select import getSelection
from login import login


mainList=['Shopping','CreditCard','BackendAdmin']
while True:
    print '''----------主菜单-----------'''
    for i in mainList:
        print '----%d\t%s-----'%(mainList.index(i)+1,i)
    print '''---------------------'''        
    if getSelection(mainList)==1:
        shopping()
    elif getSelection(mainList)==2:
        print 'CreditCard'
    else:
        print 'BackendAdmin'