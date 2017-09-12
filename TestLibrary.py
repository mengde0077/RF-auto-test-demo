# coding=utf-8
#Robot Framework test Library
#用于关键字编写联系,用于android 用户登录时输入密码，必须使用键盘键入密码，暂时默认输入密码 123456
#尽量不要用中文
"""
Version 1.6 released on 2016-09-22.
"""


import os, time, subprocess, string,datetime
from robot.api import logger
import redis
import pymysql
import ConfigParser
import hashlib
from decimal import *
import random
import requests
import urllib2
import cookielib
import re
import urlparse


def getUrlParese(url):
    #解析 获取 get url 中的请求参数
    result = urlparse.urlparse(url)
    pares = urlparse.parse_qs(result.query,True)
    return pares

def versionCompare(v1="1.1.1", v2="1.2.1"):
    v1_check = re.match("\d+(\.\d+){0,2}", v1)
    v2_check = re.match("\d+(\.\d+){0,2}", v2)
    if v1_check is None or v2_check is None or v1_check.group() != v1 or v2_check.group() != v2:
        return "版本号格式不对，正确的应该是x.x.x,只能有3段"
    v1_list = v1.split(".")
    v2_list = v2.split(".")
    v1_len = len(v1_list)
    v2_len = len(v2_list)
    if v1_len > v2_len:
        for i in range(v1_len - v2_len):
            v2_list.append("0")
    elif v2_len > v1_len:
        for i in range(v2_len - v1_len):
            v1_list.append("0")
    else:
        pass
    for i in range(len(v1_list)):
        if int(v1_list[i]) > int(v2_list[i]):
            return 1
        if int(v1_list[i]) < int(v2_list[i]):
            return -1
    return 0

def getCookieValue(url,name):
    cookie=cookielib.CookieJar()
    handler=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(handler)
    #opener.open('http://192.168.100.27:8080/captcha/image')
    opener.open(url)

    cookie_value = ''
    for x in cookie:
        if x.name == name:
            cookie_value = x.value
        return cookie_value

def monkey_patch():
    prop = requests.models.Response.content
    def content(self):
        _content = prop.fget(self)
        if self.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(_content)
            if encodings:
                self.encoding = encodings[0]
            else:
                self.encoding = self.apparent_encoding
            _content = _content.decode(self.encoding, 'replace').encode('utf8', 'replace')
            self._content = _content
        return _content
    requests.models.Response.content = property(content)


def tupleConvertList(a):
    b = list(a)
    for c in b:
        b[b.index(c)] = list(c)
    return b

def dataLen(data):
    return  len(data)

def randomString(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def weightCostPrice(weight_cost_price,stock_nums,store_cost_price,nums):
    '''
    根据输入的原总仓／微仓加权成本价、总仓／微仓库存、进货成本价／总仓加权成本价、总仓进货量／微仓进货量，来计算总仓／微仓新的加权成本价
    '''
    getcontext().rounding = ROUND_HALF_UP
    s = (weight_cost_price*stock_nums+store_cost_price*nums)/(stock_nums+nums)
    #print ("%.1f" % s)
    a = '%f'%s
    print a
    length=len(a[a.find('.'):]) 
    if length>=4: 
        p='{:.3f}'.format(Decimal(a))
        return p

def testRound(value):
    '''
    进行小数点两位的四舍五入
    '''
    a = '%f' % value
    print a
    length = len(a[a.find('.'):])
    if length>=3: 
        p='{:.2f}'.format(Decimal(a))
        return p

def getAbsoluteValue(value):
    '''
    进行取绝对值
    '''
    a = value
    print a
    b = abs(a)
    return b

def orderCommission(order_amount,sum_water=0):
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
    清除redis中的规则缓存，清除所有的缓存
    如：
    '''
    r = redis.StrictRedis(host=host, port=6379, db=0)
    r.flushall()

def redisFlushDb(host,db=0,password=""):
    '''
    清除redis中的规则缓存，清除所有的缓存
    如：
    '''
    r = redis.StrictRedis(host=host, port=6379, db=db, password=password)
    r.flushdb()

def redisDel(key,host,db=0,password=""):
    '''
    清除redis中的规则缓存，清除所有的缓存
    如：
    '''
    r = redis.StrictRedis(host=host, port=6379, db=db, password=password)
    r.delete(key)

def redisSet(key,host,db=0,password=""):
    '''
    设置一个key
    如：
    '''
    r = redis.StrictRedis(host=host, port=6379, db=db, password=password)
    r.set(key,1)

def redisHgetall(key,host,db=0,password=""):
    '''
    获取一个hash的所有值
    如：
    '''
    r = redis.Redis(host=host, port=6379, db=db, password=password)
    v = r.hgetall(key)
    print v
    return v

def redisDelKeys(key,host,db=0,password=""):
    '''
    清除 一个 以 ** 开头的 一个类型的key
    如：
    '''
    r = redis.StrictRedis(host=host, port=6379, db=db, password=password)
    cache_list = r.keys(key)
    if len(cache_list)>0:
        for i in range(len(cache_list)):
            r.delete(cache_list[i])

def redisGet(key,host,db=0,password=""):
    '''
    获取redis中key的值
    如：
    '''
    r = redis.StrictRedis(host=host, port=6379, db=db, password=password)
    v = r.get(key)
    return v

def redisDelRomotion(host,cache_list):
    '''
    清除redis中的规则缓存，测试环境活动规则验证
    如：
    '''
    r = redis.StrictRedis(host=host, port=6379, db=0)
    if len(cache_list)>0:
        for i in range(len(cache_list)):
            r.delete(cache_list[i])

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

def mysqlQueryOne(db_connect_string, sql):
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
    #mkpath="E:\\auto\\robot\\image\\8dol\\111"
    #mkdir(mkpath)
    a = randomString()
    p = testRound(3.5555)
    t = getMd5('123456')
    m = orderCommission(20,2000)
    redisDelRomotion('192.168.100.34')
    print p,t,m,a

