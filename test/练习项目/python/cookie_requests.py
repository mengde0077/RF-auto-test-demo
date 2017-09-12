#!/usr/bin python2.7
# -*- coding: utf-8 -*-


from bs4Test import *

s = requests.session()
s.get("http://192.168.100.27:8080/captcha/image")

print(s.cookies)