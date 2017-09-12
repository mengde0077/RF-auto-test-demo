#coding=utf-8

#Robot Framework test Library
#用于关键字编写联系,用于android 用户登录时输入密码，必须使用键盘键入密码，暂时默认输入密码 123456
#尽量不要用中文
"""
Version 1.4 released on 2016-02-01.
"""


import os, time, subprocess, string
import redis
import pymysql
import ConfigParser
import json
import hashlib
import random
import string

def randomString(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def weightCostPrice(weight_cost_price,stock_nums,store_cost_price,nums):
    new_weight_cost_price = (weight_cost_price*stock_nums+store_cost_price*nums)/(stock_nums+nums)
    return new_weight_cost_price

def orderCommission(order_amount, sum_water=0):
    '''
    根据输入的订单金额和水重量，来计算8仔的提成
    '''
    m = 0.0
    w = 0.0
    total_max = 5.0
    if (order_amount >= 0.0 and order_amount < 5.0):
        m = 0.50
    elif (order_amount >= 5.00 and order_amount <= 15.00):
        m += 0.50
    elif (order_amount >= 15.10 and order_amount <= 17.00):
        m += order_amount * 0.0318
    elif (order_amount >= 17.10 and order_amount <= 19.00):
        m += order_amount * 0.0304
    elif (order_amount >= 19.10 and order_amount <= 21.00):
        m += order_amount * 0.0290
    elif (order_amount >= 21.10 and order_amount <= 23.00):
        m += order_amount * 0.0277
    elif (order_amount >= 23.10 and order_amount <= 25.00):
        m += order_amount * 0.0265
    elif (order_amount >= 25.10 and order_amount <= 27.00):
        m += order_amount * 0.0253
    elif (order_amount >= 27.10 and order_amount <= 29.00):
        m += order_amount * 0.0241
    elif (order_amount >= 29.10 and order_amount <= 31.00):
        m += order_amount * 0.0231
    elif (order_amount >= 31.10 and order_amount <= 33.00):
        m += order_amount * 0.0220
    elif (order_amount >= 33.10 and order_amount <= 35.00):
        m += order_amount * 0.0210
    elif (order_amount >= 35.10 and order_amount <= 40.00):
        m += order_amount * 0.0201
    elif (order_amount >= 40.10 and order_amount <= 50000.00):
        m += order_amount * 0.0200
    else:
        return 'order_amount error'
    if sum_water < 1000:
        w = 0.0
    elif sum_water == 1000:
        w = 0.1
    elif sum_water > 1000:
        w = 0.1 + ((sum_water-1000)/500)*0.1
    else:
        return 'sum_sum_water error'
    s = '%f'%m   
    mv_s = s[:-5]
    m = string.atof(mv_s)
    if((m+w) <= 5.0):
        return (m+w)
    else:
        return total_max

def getMd5(v):
    """
    input   字符串
    返回字符串的MD5值
    """
    m2 = hashlib.md5()
    m2.update(v)
    t = m2.hexdigest()
    return t

def dolPassWord(passWord=""):
    """
    input   passWord
     123456
    """
    cmd = "adb shell input keyevent 8"
    s = subprocess.check_output(cmd.split())
    cmd = "adb shell input keyevent 9"
    s = subprocess.check_output(cmd.split())
    cmd = "adb shell input keyevent 10"
    s = subprocess.check_output(cmd.split())
    cmd = "adb shell input keyevent 11"
    s = subprocess.check_output(cmd.split())
    cmd = "adb shell input keyevent 12"
    s = subprocess.check_output(cmd.split())
    cmd = "adb shell input keyevent 13"
    s = subprocess.check_output(cmd.split())

def backKey():
    """
    按一下返回键
    """
    cmd = "adb shell input keyevent 4"
    s = subprocess.check_output(cmd.split())

def getNowTime():
    '''
    get new strTime :2015-11-03 16:57:15
    '''
    ISOTIMEFORMA = '%Y-%m-%d %X'
    t = time.strftime(ISOTIMEFORMA, time.localtime())
    return t

def getStrTime():
    '''
    get new strDate :235959
    '''
    ISOTIMEFORMA = '%H%M%S'
    t = time.strftime(ISOTIMEFORMA, time.localtime())
    return t

def getStrDate():
    '''
    get new strDate :20151103
    '''
    ISOTIMEFORMA_1 = '%Y%m%d'
    t = time.strftime(ISOTIMEFORMA_1, time.localtime())
    return t

def mkdir(path):
    '''
    path = "E:\\auto\\robot\\image\\8dol\\111"
    '''
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

def redisFlushAll(host):
    '''
    清除redis中的规则缓存，测试环境活动规则验证
    如：
    '''
    r = redis.StrictRedis(host=host, port=6379, db=0)
    time.sleep(3)
    r.flushall()

def readConfig(ConfigFile):
    '''
    读取配置文件，获取配置信息，暂时未完善
    如：
    name='touch_me_today_set.20151120'
    '''
    config = ConfigParser.ConfigParser()
    config.read([ConfigFile])

def connectMysql(db_connect_string):
    '''
    连接mysql数据库，默认为测试库
    如：
                    host='121.41.51.178',
                    user='sale',
                    password='sale',
                    database='saledb'
    '''
    db_connect_string = "pymysql.connect(%s,charset='utf8')" % db_connect_string
    conn = eval(db_connect_string)
    return conn

def mysqlQueryOne(db_connect_string,sql):
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

def mysqlQueryAll(db_connect_string, sql):
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

def mysqlExecute(db_connect_string, sql):
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

def mysqlClose(conn):
    '''
    断开连接mysql数据库
    '''
    conn = connectMysql()
    conn.close()


if __name__ == '__main__':
    # mkpath="E:\\auto\\robot\\image\\8dol\\111"
    # mkdir(mkpath)
    # json_str = '{"result":"ok","msg":"操作成功","code":200,"data":{"store_goods_category":[{"code":"SINGLE","name":"单品"},{"code":"BUNDLE","name":"套餐"}],"store_basic_info":{"store_id":64,"store_user_name":"测试账号","store_user_id":4223,"status_name":"Opening","store_user_mobile":"12312312312","store_short_desc":"","store_name":"zllyd的小店","store_img":"","status_img":"http"}},"rescode":200}'
    # json_string = '{"favorited": false, "contributors": null}'
    # db_connect_string = "host='121.41.51.178',user='sale',password='sale',db='saledb',port=3306"
    # jsonResolve(json_string)
    # sql = "select * from t_user_states t where t.id=1514174"
    # v = mysqlQueryAll(db_connect_string,sql)
    # print json
 #   t = getMd5('123456')
#    m = orderCommission(20,2000)
    #host = '192.168.100.19'
    #delRedisFlushAll(host)
    #p = weightCostPrice(12.9,3,11.4,5)
    p = randomString()
    print p

