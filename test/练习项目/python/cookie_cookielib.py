#!/usr/bin python2.7
# -*- coding: utf-8 -*-


import urllib2
import cookielib

cookie=cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
opener.open('http://192.168.100.27:8080/captcha/image')

print cookie
cookie_value = ''
for x in cookie:
    if x.name == '__cfduid':
        cookie_value = x.value
    break