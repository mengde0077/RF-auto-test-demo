#!/usr/bin python2.7
# -*- coding: utf-8 -*-

import threading, datetime, time, httplib

# 初始最大并发数
START_THEAD_COUNT = 200

# 递增并发数
THREAD_INCREASE_STEP = 10

# 域名
DOMAIN = 'www.baidu.com'

# 默认http请求
METHOD = 'get'

# 默认访问的web路径
PATH = '/'

# 请求发送间隔 整数
INTERVAL = 5 # 5秒

'''Factory'''
class biz :

    '''Main'''
    def run(self) :
        start = datetime.datetime.now()
        global FAILED_COUNT
        FAILED_COUNT = 0
        threads = []
        # thread instance initialization
        for i in range(START_THEAD_COUNT) :
            t=threading.Thread(target=self.execute, args=())
            threads.append(t)
            # activate threads
            for i in range(START_THEAD_COUNT) :
                threads[i].start()
                # wait for all ends
                for i in range(START_THEAD_COUNT) :
                    threads[i].join()
                    delta = datetime.datetime.now() - start
                    writeline('INFO', 'Total is \'' + str(START_THEAD_COUNT) + '\' while failed \'' + str(FAILED_COUNT) + '\' in ' + str(delta.seconds) + str(delta.microseconds / 1000) + 'ms.')
                    return (True, None)

    
    '''Execute http request and get response status'''
    def execute(self) :
        global FAILED_COUNT
        conn = httplib.HTTPConnection(DOMAIN)
        conn.request(METHOD, PATH)
        r = conn.getresponse()
        if r.status not in (200, 302) : FAILED_COUNT = FAILED_COUNT + 1
        conn.close()
        return (True, None)

    '''Log writer'''
    def writeline(status, msg) :
        line = time.strftime('%Y-%m-%d %X', time.localtime(time.time())) + ' [' + status + '] ' + msg
        print line
        return (True, line)

if __name__ == '__main__' :
    o = biz()
    while True :
        r, c = o.run()
        if not r : writeline('FAILED-', c)
        time.sleep(INTERVAL)
        # update max threads
        START_THEAD_COUNT = START_THEAD_COUNT + THREAD_INCREASE_STEP