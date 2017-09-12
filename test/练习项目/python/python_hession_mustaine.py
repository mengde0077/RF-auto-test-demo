#!/usr/bin/python

# coding=utf-8
from mustaine.client import HessianProxy

serviceUrl = 'http://192.168.100.35:20880/com.edol.core.inf.rule.PromotionInterface'

costType = 'BALANCE'
messageType = 'BALANCE_LOTTERY_COUPON'
numberFlag = 'true'

if __name__ == '__main__':
     proxy = HessianProxy(serviceUrl)
     result = proxy.findTurntableLotteryByCostType(costType, messageType, numberFlag)
     print result
