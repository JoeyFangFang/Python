#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang
from sqlhandle import SQL_Change,SQL_Del,SQL_Insert,SQL_Select
'''def Create_CardAccount():
    '添加信用卡账户'
    username = raw_input('Please input a new username--->')
    if not Select_CardAccount(username):
        while True:    
            password = raw_input("Please input the password --->")
            check_pwd = raw_input("Please input the password again --->")
            if password == check_pwd:
                break
            else:
                print "The check password is not the same as the password"
        sql2 = 'INSERT into creditcardusers values (?,?,?)'
        params2 = (username,password,'unlocked')
        Db_Insert(sql2, params2)
    else:
        print 'the account %s exists'%username
'''        
'''动态查询多个表，采用string拼接得到SQL语句
        如：sql = "select * from %s" %tablename
      sql1 = 'where %s = ?'%option
      param = ('book1',)  
      sql2 = sql + sql1
      cur.execute(sql2,param)
      == select * from TABLENAME where OPTION = 'book1'
        '''

def Select_Item(tablename,option,v):
    '查找表信息'
    sql = "select * from %s where %s=(?)"%(tablename,option)
    params = (v,)
    result = SQL_Select(sql, params)
    return result

def Change_Item(tablename,option,chkey,v):
    '''修改表数据
    @param tablename:表名
    @param option:查找项
    @param chkey:修改项
    @param v:(修改后值，查询条件值)    
    '''
    sql = 'update %s SET %s = ? where %s = ?'%(tablename,chkey,option)
    params = (v,)
    print sql,params
    SQL_Change(sql,params)

def Insert_Item(tablename,**v):
    '''增加表数据
    @param tablename:表名
    @param v: 字典形式的一行数据 
    '''
    k =tuple(v.keys())
    v=tuple(v.values())
    sql = 'insert into %s %s values %s'%(tablename,k,v)
    print sql
    SQL_Insert(sql)

def Del_Item(tablename,option,v):
    '删除表信息'
    sql = "delete from %s where %s = ?"%(tablename,option)
    params =(v,)
#    print sql,params
    SQL_Del(sql, params)

#Insert_Item('goodsdb',**{'name':'laptop','price':'6000','stocks':20})    
#Del_Item('goodsdb', 'name', 'SDcard')