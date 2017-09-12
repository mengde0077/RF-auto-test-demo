# -*- coding: utf-8 -*-
# @Author: caolinming
# @Date:   2017-09-01 16:54:39
# @Last Modified by:   caolinming
# @Last Modified time: 2017-09-04 14:01:38
import redis
from robot.api import logger

class RedisKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'


    def _connectRedis(self, host,db=0,password=""):
        logger.debug("connect redis: host = %s ,port = 6379, db = %s, password = %s " % (host, db, password))
        return  redis.StrictRedis(host=host, port=6379, db=db, password=password)


    def redisFlushAll(self, host,password=""):
        '''
        清除redis中的规则缓存，清除所有的缓存
        如：
        '''
        r = self._connectRedis(host=host, password=password)
        r.flushall()

    def redisFlushDb(self, host,db=0,password=""):
        '''
        清除redis中的规则缓存，清除所选db中所有的缓存
        如：
        '''
        r = self._connectRedis(host=host, db=db, password=password)
        r.flushdb()

    def redisDel(self, key,host,db=0,password=""):
        '''
        清除redis中的规则缓存，删除指定的key
        如：
        '''
        r = self._connectRedis(host=host, db=db, password=password)
        r.delete(key)

    def redisSet(self, key,host,db=0,password=""):
        '''
        设置一个key
        如：
        '''
        r = self._connectRedis(host=host, db=db, password=password)
        r.set(key,1)

    def redisHgetall(self, key,host,db=0,password=""):
        '''
        获取一个hash的所有值
        如：
        '''
        r = redis.Redis(host=host, port=6379, db=db, password=password)
        v = r.hgetall(key)
        print v
        return v

    def redisDelKeys(self, key,host,db=0,password=""):
        '''
        清除 一个 以 ** 开头的 一个类型的key
        如：
        '''
        r = self._connectRedis(host=host, db=db, password=password)
        cache_list = r.keys(key)
        if len(cache_list)>0:
            for i in range(len(cache_list)):
                logger.debug("del key:  %S " % cache_list[i])
                r.delete(cache_list[i])

    def redisGet(self, key,host,db=0,password=""):
        '''
        获取redis中key的值
        如：
        '''
        r = self._connectRedis(host=host, db=db, password=password)
        v = r.get(key)
        return v

    def redisDelRomotion(self, host, cache_list):
        '''
        清除redis中的规则缓存，测试环境活动规则验证
        如：
        '''
        r = self._connectRedis(host=host)
        if len(cache_list)>0:
            for i in range(len(cache_list)):
                r.delete(cache_list[i])


