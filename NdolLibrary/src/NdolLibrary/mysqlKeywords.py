# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-09-04 16:27:13
# @Last Modified by:   caolinming
# @Last Modified time: 2017-09-04 17:24:42

from robot.api import logger
import pymysql

class MysqlKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'


    def connectMysql(self, db_connect_string):
        '''
        连接mysql数据库，默认为测试库
        如：
        	host='121.41.51.178',
        	user='sale',
        	password='sale',
        	database='saledb'
        '''
        db_connect_string = "pymysql.connect(%s,charset='utf8')" % db_connect_string
        logger.debug("db_connect_string: %s" % db_connect_string)
        conn = eval(db_connect_string)
        return conn


    def mysqlQueryOne(self, db_connect_string, sql):
	    '''
	    执行查询语句，只返回一条数据
	    如：
	            sql = 'select * from t_rules'
	    '''
	    try:
	        conn = connectMysql(db_connect_string)
	        with conn.cursor() as cursor:
	            # Read a single record
	            cursor.execute(sql)
	            result = cursor.fetchone()
	            return result
	    finally:
	        conn.close()


    def mysqlQueryAll(self, db_connect_string, sql):
	    '''
	    执行查询语句，并返回全部的数据
	    如：
	            Mysql Query All     'select * from t_rules'
	    '''
	    try:
	        conn = connectMysql(db_connect_string)
	        with conn.cursor() as cursor:
	            # Read a single record
	            cursor.execute(sql)
	            result = cursor.fetchall()
	            return result
	    finally:
	        conn.close()


    def mysqlExecute(self, db_connect_string, sql):
	    '''
	    执行需要提交的SQL语句，没有返回值
	    如：
	    如：
	            sql = 'delete from t_rules where **'
	            sql = 'insert into t_rules VALUES(**,**,**)'
	            sql = 'update t_rules set **=**'
	    '''
	    try:
	        conn = connectMysql(db_connect_string)
	        with conn.cursor() as cursor:
	            cursor.execute(sql)
	        conn.commit()
	    finally:
	        conn.close()


    def mysqlClose(self, conn):
	    '''
	    断开连接mysql数据库
	    '''
	    conn = connectMysql()
	    conn.close()
