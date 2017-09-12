# coding=utf-8
'''
Created on 2015年11月1日
 
@author: caolinming
'''

import pymysql




def connectMysql(host='121.41.51.178',
                    user='sale',
                    password='sale',
                    database='saledb',
                    port=3306):
    '''
    连接mysql数据库，默认为测试库
    如：
                    host='121.41.51.178',
                    user='sale',
                    password='sale',
                    database='saledb'
    ''' 
    conn = pymysql.connect(host=host,
                    user=user,
                    passwd=password,
                    db=database,
                    port=port,
                    charset='utf8')
    return  conn

def mysqlQueryOne(conn,sql):
    '''
    连接mysql数据库，默认为测试库
    如：
			sql = 'select * from t_rules'
    ''' 
    try:
        with conn.cursor() as cursor:
            # Read a single record
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        conn.close()

def mysqlQueryAll(conn,sql):
    '''
    连接mysql数据库，默认为测试库
    如：
			sql = 'select * from t_rules'
    ''' 
    try:
        with conn.cursor() as cursor:
            # Read a single record
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        conn.close()  
                 

def mysqlExecute(conn,sql):
    '''
    连接mysql数据库，默认为测试库
    如：
			sql = 'delete from t_rules where **'
			sql = 'insert into t_rules VALUES(**,**,**)'
			sql = 'update t_rules set **=**'			
    ''' 
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()

    finally:
        conn.close()  
              

def mysqlClose(conn):
    '''
    断开连接mysql数据库
    ''' 
    conn.close()          
        
if __name__ == '__main__':
    conn = connectMysql()
    sql = 'select * from t_rules'
    result = mysqlQueryOne(conn,sql)
    print result
    #mysqlClose(conn) 