# @Author: caolinming
# @Date:   2016-07-20 19:48:37
# @Last Modified by:   caolinming
# @Last Modified time: 2017-06-23 17:56:19

#参考   https://testerhome.com/topics/599
#显示链接的设备
#adb devices > MonkeyTest.txt

# 在有设备连接的前提下，在命令行中输入：adb shell 进入shell界面
#adb shell

#查看data/data文件夹下的应用程序包。注：我们能测试的应用程序包都在这个目录下面
# ls data/data

# -v –v -v  打印最详细的3级日志
#adb shell monkey -p com.ndol.sale.starter -v –v -v 10000 >> MonkeyTest.txt

#adb shell monkey -p com.ndol.sale.starter --pct-majornav 50 1000
#adb shell monkey -p com.ndol.sale.starter --pct-anyevent 100 1000
#adb shell monkey -p com.ndol.sale.starter --pct-appswitch 70 1000

#调整“系统”按键事件的百分比
#adb shell monkey -p com.ndol.sale.starter --pct-syskeys 60 1000

#运行多个APP
#adb shell monkey -p com.ndol.sale.starter -p com.ndol.b2b.cloud --pct-syskeys 60 1000

#运行异常，kill掉 monkey
#adb shell ps|grep monkey
#adb shell kill -9 pid

###测试报告处理

#根据第二步的命令最后把测试日志重定向到了文件XXX.txt,到你执行monkey测试的目录下把文件找出来打开查看，
#分别搜索 exception ， anr ， crash 三个关键词，如果搜索结果有发现这些关键词，则把该日志文件发送给相关的android程序员进行处理。
#如果未搜索到这些关键字，则说明此次测试结果较理想，没发现异常，以后可以再接着测试。



adb shell monkey -p com.ndol.sale.starter --pct-majornav 30 --pct-syskeys 20 --pct-touch 35 --pct-motion 5 --pct-trackball 5 --pct-appswitch 5 -s 12867 --ignore-crashes -v -v -v --throttle 300 2000 1 >> MonkeyTest.txt 2>&1 &

