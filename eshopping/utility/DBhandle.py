#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang

from sqlhandle import SQL_Change,SQL_Del,SQL_Select,SQL_Insert,Get_Field

def Select_All(tablename):
    '查找所有表数据'
    sql = "select * from %s"%tablename
    params =''
    result = SQL_Select(sql, params)
    return result

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
    SQL_Change(sql,params)

def Insert_Item(tablename,**itemdict):
    '''增加表数据
    @param tablename:表名
    @param v: 字典形式的一行数据 
    '''
    keys,values = zip(*itemdict.items())
    #k =tuple(v.keys())
    #v=tuple(v.values())
    sql  = 'INSERT INTO %s (%s) values (%s)'%(tablename,",".join(keys),",".join(['?']*len(keys)))
    params = values
    SQL_Insert(sql,params)

def Del_Item(tablename,option,v):
    '删除表信息'
    sql = "delete from %s where %s = ?"%(tablename,option)
    params =(v,)
    SQL_Del(sql, params)
    
def Get_TableField(tablename):
    '获取表字段名'
    sql = "PRAGMA table_info(%s)"%tablename
    return Get_Field(sql)
    
