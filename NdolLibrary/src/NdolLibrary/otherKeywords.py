# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-09-04 16:27:37
# @Last Modified by:   caolinming
# @Last Modified time: 2017-09-04 18:03:56

import os, time, subprocess, string,datetime
from robot.api import logger
import ConfigParser
import hashlib
from decimal import *
import random
import requests
import urllib2
import cookielib
import re
import urlparse

class OtherKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def getUrlParese(self, url):
	    #解析 获取 get url 中的请求参数
	    result = urlparse.urlparse(url)
	    pares = urlparse.parse_qs(result.query,True)
	    return pares


    def getCookieValue(self, url,name):
	    '''
	    获取url的cookies中指定key的值
	    '''
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


    def monkey_patch(self):
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


    def tupleConvertList(self, a):
	    b = list(a)
	    for c in b:
	        b[b.index(c)] = list(c)
	    return b


    def dataLen(self, data):
	    '''
	    返回给定字符串的长度
	    '''
	    return  len(data)


    def randomString(self, size=12, chars=string.ascii_uppercase + string.digits):
	    '''
	    返回指定长度的随机字符串
	    '''
	    return ''.join(random.choice(chars) for _ in range(size))


    def weightCostPrice(self, weight_cost_price,stock_nums,store_cost_price,nums):
	    '''
	    根据输入的原总仓／微仓加权成本价、总仓／微仓库存、进货成本价／总仓加权成本价、总仓进货量／微仓进货量，来计算总仓／微仓新的加权成本价
	    '''
	    getcontext().rounding = ROUND_HALF_UP
	    s = (weight_cost_price*stock_nums+store_cost_price*nums)/(stock_nums+nums)
	    #print ("%.1f" % s)
	    a = '%f'%s
	    print a
	    length=len(a[a.find('.'):]) 
	    if length >= 4: 
	        p = '{:.3f}'.format(Decimal(a))
	        return p


    def testRound(self, value):
	    '''
	    进行小数点两位的四舍五入
	    '''
	    a = '%f' % value
	    print a
	    length = len(a[a.find('.'):])
	    if length >= 3: 
	        p = '{:.2f}'.format(Decimal(a))
	        return p


    def getAbsoluteValue(self, value):
	    '''
	    进行取绝对值
	    '''
	    a = value
	    print a
	    b = abs(a)
	    return b

    def orderCommission(self, order_amount,sum_water=0):
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


    def getMd5(self, string):
	    """
	    input   字符串
	    返回字符串的MD5值
	    """
	    m2 = hashlib.md5()
	    m2.update(string)
	    t = m2.hexdigest()
	    return t


    def getNowTime(self):
	    '''
	    get new strTime :2015-11-03 16:57:15
	    '''
	    ISOTIMEFORMA = '%Y-%m-%d %X'
	    t = time.strftime(ISOTIMEFORMA, time.localtime())
	    return t


    def getStrTime(self):
	    '''
	    get new strDate :235959
	    '''
	    ISOTIMEFORMA = '%H%M%S'
	    t = time.strftime(ISOTIMEFORMA, time.localtime())
	    return t


    def getStrDate(self):
	    '''
	    get new strDate :20151103
	    '''
	    ISOTIMEFORMA_1 = '%Y%m%d'
	    t = time.strftime(ISOTIMEFORMA_1, time.localtime())
	    return t


    def mkdir(self, path):
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

    def dolPassWord(self, passWord=""):
	    """
	    通过点击android手机软键盘 输入   passWord
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


    def backKey(self):
	    """
	    按一下android手机返回键
	    """
	    cmd = "adb shell input keyevent 4"
	    s = subprocess.check_output(cmd.split())


    def versionCompare(self, v1="1.1.1", v2="1.2.1"):
    	'''
    	比对app的版本号
    	'''
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


