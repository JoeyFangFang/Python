#_*_ coding:utf-8 _*_
'''判断选择是否正确'''

import re

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
        
def getSelection2(s_dict):
    '''物品选择'''
    while True:
        a= list(enumerate(s_dict,1))
        for item in a:
            print '%d\t%s\t%s'%(item[0],item[1],s_dict[item[1]])
        selection = raw_input('Please enter the Goods Number what do you want to buy?(1~ %d)'%len(s_dict))
        if isValidNum(selection):
            if isValidSelection(int(selection),s_dict):
                return a[int(selection)-1]
            else:
                print '[Warning]Please input a valid Selection!'
                continue
        print '[Warning]Please input a valid interge!'