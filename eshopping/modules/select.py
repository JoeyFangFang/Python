#_*_ coding:utf-8 _*_
'''判断选择是否正确'''

import re
import json
from eshopping.config.config import GoodsDBFile

#判断输入数字是否有效
def isValidNum(num):
    return True if re.match(r'\d+',num) else False

#判断选项是否是有效选择
def isValidSelection(select,s_list):
    try:
        if 0<select<=len(s_list):
            return True
        else:
            return False
    except:
        print '[Warning]Please input a valid interge!'
        
def getSelection(s_list):
    '''选项选择'''
#    print s_list
    while True:
        selection = raw_input('Please enter the Selection ?(1~ %d)'%len(s_list))
        if isValidNum(selection):
            if isValidSelection(int(selection),s_list):
                return int(selection)
            else:
                print '[Warning]Please input a valid Selection!'
                continue
        print '[Warning]Please input a valid interge!'
        
def getItem():
    '''购物商品选择'''
    goodsDict = json.load(open(GoodsDBFile,'r'))
    while True:
        for item in goodsDict:
            print '\t{0:5}\t{1:5}\t{2:5}\t{3:5}'.format(item,*goodsDict[item])
        selection = raw_input('Please input the Item Number what do you want to buy?')
        if selection in goodsDict:
            return selection
        else:
            print 'Please input the correct Item Number!'