# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2016-07-22 11:40:57
# @Last Modified by:   caolinming
# @Last Modified time: 2016-07-22 13:49:40


#!/usr/local/android-sdk-macosx/tools/monkeyrunner
#导入python中自带的time模块和sys模块，脚本中都要用到它们。
import time
import sys
#MonkeyRunner自带的三个apifrom com.android.monkeyrunner
import MonkeyRunner,MonkeyDevice,MonkeyImage
#这个函数时确认年月日时分秒
now=time.strftime("%Y-%m-%d-%H-%M-%S")
#指定我们要保存图片的位置和打印log的位置
path='D:\\picture\\'
logpath="D:\\log\\"
#python中获取当前运行的文件的名字
name=sys.argv[0].split("\\")
filename=name[len(name)-1]

print(name)
print(filename)

#新建一个log文件
log=open(logpath+filename[0:-3]+"-log"+now+".txt",'w')
#连接设备，两个参数分别是等待的时间(这里的时间都是秒为单位)，设备的序列号。
device=MonkeyRunner.waitForConnection(5,'b4726a2d')
#安装锤子便签apk。参数是apk文件的位置，因为python不支持中文输入，所以在后面用了.decode('utf-8')这个方法转码。
device.installPackage ('D:\\apk\\锤子便签.apk'.decode('utf-8'))
#打印出操作信息到log文件里
log.write("安装apk……\n")
#等待2秒
MonkeyRunner.sleep(2)
#启动app，参数里是app的包名/活动名
device.startActivity(component='com.smartisan.notes/.NotesActivity')
MonkeyRunner.sleep(2)
#打印操作信息
log.write("启动app……\n")
#截图
result = device.takeSnapshot()
#保存截图
result.writeToFile(path+"主页面".decode('utf-8')+now+'.png','png')
#点击搜索款的位置坐标。
device.touch(111,155,'DOWN_AND_UP')
MonkeyRunner.sleep(2)
#输入smartisan字样
device.type("smartisan")
#截图
result1=device.takeSnapshot()
#保存截图
result1.writeToFile(path+"搜索框截图".decode('utf-8')+'.png','png')
#移动第一个便签的位置到最后面去，参数是：一个起始点坐标，一个终点坐标，移动的时间，移动的步骤
device.drag((232,235),(216,472),3,2)
MonkeyRunner.sleep(3)
#截图
result2=device.takeSnapshot()
#保存截图
result2.writeToFile(path+"移动便签".decode('utf-8')+now+".png",'png')
#第一个便签向右滑动
device.drag((109,360),(322,360))
MonkeyRunner.sleep(3)
#截图
result3=device.takeSnapshot()
#保存截图
result3.writeToFile(path+"右移动便签".decode('utf-8')+now+".png",'png')
#点击最后一个便签的位置
device.touch(182,583,'DOWN_AND_UP')
MonkeyRunner.sleep(5)
#点击发送的位置
device.touch(324,73,'DOWN_AND_UP')
MonkeyRunner.sleep(5)
#点击发送至长微博的位置
device.touch(227,789,'DOWN_AND_UP')
MonkeyRunner.sleep(5)
#点击生成长微博的位置
device.touch(228,791,'DOWN_AND_UP')
MonkeyRunner.sleep(5)
#截图
result4=device.takeSnapshot()
#保存图片
result4.writeToFile(path+"发长微博截图".decode("utf-8")+now+'.png','png')
#点击下一步的位置
device.touch(426,81,'DOWN_AND_UP')
MonkeyRunner.sleep(3)
#截图
result5=device.takeSnapshot()
#保存截图
result5.writeToFile(path+"输入微博账号".decode("utf-8")+now+'.png','png')
#点击输入微博账号和密码的几个位置，分别输入账号和密码
device.touch(196,311,'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.type("powermo@126.com")
MonkeyRunner.sleep(3)
device.touch(168,378,'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.type("powermo1234")
MonkeyRunner.sleep(3)
#点击登录
device.touch(237,449,'DOWN_AND_UP')
MonkeyRunner.sleep(3)
#截图
result6=device.takeSnapshot()
#保存截图
result6.writeToFile(path+"登陆微博".decode("utf-8")+now+'.png','png')
#下面就开始对之前的截图进行对比了
#第一张截图做对比，去文件中找到我们要对比的图片
resultTrue=MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue.png')
log.write("主页面对比图片……\n")
#判断图片相识度是否是为90%
if(result.sameAs(resultTrue,0.9)):
    #在命令行打印出信息
    print("主页面图片对比成功")
    #打印信息到log文件
log.write("主页面图片对比成功……\n")
else:
    #打印信息到命令行
    print("主页面图片对比失败")
    log.write("主页面图片对比失败……\n")

#去文件中找到我们规定的图片用来对比
result1True=MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue1.png')
#判断图片相识度是否是为90%
if(result1.sameAs(result1True,0.9)):
    print("搜索框图片对比成功")
    log.write("搜索框图片对比成功……\n")
else:
    print("搜索框图片对比失败")
    log.write("搜索框图片对比失败……\n")

#对移动便签图片对比
result2True=MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue2.png')
#判断图片相识度是否是为80%
if(result2.sameAs(result2True,0.8)):
    print("移动便签对比成功")
    log.write("移动便签对比成功……\n")
else:
    print("移动便签图片对比失败")
    log.write("移动便签对比失败……\n")

#对移动便签图片进行对比，去文件中找我们规定的图片
result3True=MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue3.png')
#判断图片相识度是否是为80%
if(result3.sameAs(result3True,0.8)):
    print("右移便签图片对比成功")
    log.write("右移便签图片对比成功……\n")
else:
    print("右移便签图片对比失败")
    log.write("右移便签图片对比失败……\n")

#对长微博图片对比
result4True=MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue4.png')
if(result4.sameAs(result4True,0.8)):
    print("发长微博图片对比成功")
    log.write("发长微博图片对比成功……\n")
else:
    print("发长微博图片对比失败")
    log.write("发长微博图片对比失败……\n")

result5True=MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue5.png')
if(result5.sameAs(result5True,0.8)):
    print("输入微博账号图片对比成功")
    log.write("输入微博账号图片对比成功……\n")
else:
    print("输入微博账号图片对比失败")
    log.write("输入微博账号图片对比失败……\n")

result6True=MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue6.png')
if(result6.sameAs(result6True,0.8)):
    print("登陆微博图片对比成功")
    log.write("登陆微博图片对比成功……\n")
else:
    print("登陆微博图片对比失败")
    log.write("登陆微博图片对比失败……\n")