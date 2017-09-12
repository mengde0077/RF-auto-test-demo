from pyhessian.client import HessianProxy
service = HessianProxy("http://hessian.caucho.com/test/test")
print service.replyDate_1()