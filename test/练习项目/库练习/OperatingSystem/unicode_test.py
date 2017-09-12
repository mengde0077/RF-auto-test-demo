# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-07-05 10:13:55
# @Last Modified by:   caolinming
# @Last Modified time: 2017-07-06 10:16:57

import json

data_dict = {
'name' : '曹林明',
'shares' : 100,
'price' : 542.23
}

# json_str = json.dumps(data_dict)
# print "data_dict_type = " + str(type(data_dict))   # 'dict'
# print "data_dict = " + str(data_dict)
# print data_dict
# print "data_dict.name = " + data_dict['name']
# print "json_str_type = " + str(type(json_str))     # 'str'
# print "json_str = " + json_str
# # print json_str['name']   #不是 字典
# data = json.loads(json_str)
# print "data = " + str(data)
# print data
# print data['name']


#参考 http://www.jb51.net/article/96566.htm
#如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
#编码成JSON数据
f = open('rule_data.json', 'r')
print f
content = json.load(f)
# print content
print content['rulesAreas'][0]['name']
# dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort_keys=False, **kw)
# 拼接json数据，转码为非ascii编码    
#sort_keys 关键字 按字母排序，indent 缩进位数，ensure_ascii 是否转换ascii码
# skipkeys 跳跃键？？， allow_nan  ？？
jsdata = json.dumps(content, sort_keys=True, indent=0, ensure_ascii=False)
print jsdata
f.close()


# json_str2 = json.dumps(data_dict, ensure_ascii = False).encode('utf8')
# print data_dict2




s = "人生苦短"
print s
# ： su是一个utf-8格式的字节串
u  = s.decode("utf-8")
print u
# ： s被解码为unicode对象，赋给u
sg = u.encode("gbk")
# ： u被编码为gbk格式的字节串，赋给sg
print sg
# 打印sg



