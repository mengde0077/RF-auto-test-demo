# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-06-30 15:38:45
# @Last Modified by:   caolinming
# @Last Modified time: 2017-06-30 15:49:04


#appium 微信h5自动化示例
from appium import webdriver
import time

packageName='com.tencent.mm'
appActivity='.ui.LauncherUI'

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'f4301fe8'
desired_caps['appPackage'] = packageName
desired_caps['appActivity'] = appActivity
desired_caps['fullReset'] = 'false'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
desired_caps['fastReset'] = 'false'

desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}   #驱动H5自动化关键之一

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(30)
driver.find_element_by_name('我').click()
print driver.contexts
driver.find_element_by_name('相册').click()
driver.find_element_by_xpath("//*[contains(@text,'正在繁星直播')]").click()
print driver.current_context
driver.find_element_by_xpath("//*[contains(@text,'正在繁星直播')]").click()
print driver.current_context
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
print driver.current_context
print driver.page_source
driver.find_element_by_xpath('//*[@id="btnRecommend"]/div[1]').click()
driver.switch_to_default_content()
time.sleep(2)
driver.quit()