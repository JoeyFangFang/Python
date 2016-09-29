#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#Author:JoeyFang

'''数据库处理（sqlite3）
数据库：BASEDIR/utility/eshopping.db3
表：
'''
import os
import sqlite3
db_file = ''.join([os.path.dirname(__file__),os.sep,'eshopping.db3'])

def SQL_Insert(sql,params):
    print sql,params
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(sql,params)
    conn.commit()
    cur.close()
    conn.close()      
#删
def SQL_Del(sql,params):
    print sql,params
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(sql,params)
    conn.commit()
    cur.close()
    conn.close()  
#改
def SQL_Change(sql,params):
    print sql,params
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.executemany(sql,params)
    conn.commit()
    cur.close()
    conn.close()  
#查
def SQL_Select(sql,params):
    print sql,params
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(sql,params)
    result = cur.fetchall()
    cur.close()
    conn.close()  
    return result

#获取table字段名
def Get_Field(sql):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    tablefield = []
    for item in result:
        tablefield.append(item[1])
    cur.close()
    conn.close()
    return tablefield  


    '''cur.execute('Create table if not exists goodsdb(id integer primary key autoincrement,name varchar(30),price integer, stocks integer )')
    cur.execute("Insert into  goodsdb Values (NULL,'PC',5000,10)")
    goodsinfo = [
                ("Mobile", 2300, 50),
                ("Mp3", 420, 100),
                ("SDcard", 50, 200),
                ("Bike", 860, 21),
                ]
    cur.executemany("insert into goodsdb(name,price,stocks) Values (?,?,?)",goodsinfo)'''