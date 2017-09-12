# -*- coding:utf-8 -*-
from pyhessian.client import HessianProxy
from pyhessian import protocol
import json
def InvokeHessian(service,interface,method,req,retcode='200'):
    try:
        url='http://192.168.100.35:20880/'+service+'.'+interface
        
        print 'URL:\t%s'%url
        print 'Method:\t%s'%method
        print 'Req:\t%s'%req
        res=getattr(HessianProxy(url),method)(req)
        print 'Res:\t%s'%json.dumps(res,ensure_ascii=False)
        
    except Exception,e:
        print e
       
if __name__ == '__main__':
    service='core_service'
    interface='com.edol.core.inf.rule.PromotionInterface'
    method='findTurntableLotteryByCostType'
    req=protocol.object_factory('com.edol.core.inf.rule.PromotionInterface.findTurntableLotteryByCostType',
                                costType='BALANCE',messageType='BALANCE_LOTTERY_COUPON',numberFlag='true')
    
    InvokeHessian(service, interface, method,req)