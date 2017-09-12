# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-06-22 15:42:43
# @Last Modified by:   caolinming
# @Last Modified time: 2017-06-22 15:47:40



import re

def versionCompare(v1="1.1.1", v2="1.2"):
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
            return "v1大"
        if int(v1_list[i]) < int(v2_list[i]):
            return "v2大"
    return "相等"

# 测试用例
print(versionCompare(v1="", v2=""))
print(versionCompare(v1="1.0.a", v2="d.0.1"))
print(versionCompare(v1="1.0.1", v2="1.0.1"))
print(versionCompare(v1="1.0.2", v2="1.0.1"))
print(versionCompare(v1="1.0.1", v2="1.0.2"))
print(versionCompare(v1="1.0.11", v2="2.0.2"))