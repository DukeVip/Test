import logging

from redis import Redis

logger = logging.getLogger('django')
redis = Redis(host='127.0.0.1', port=6379)


def log_client_ip(func):  #定义装饰器，在日志中添加访问用户IP(
    def wrap(request):
        host = request.get_host()
        logger.info(host)
        return func(request)
    return wrap
#需要在setting中配置logging
#logging.DEBUG INFO ,WARN ,ERROR ,CRITICAL
#logger.info('abcd) logger.debug(something)
#tail -f debug.log 监视日志信息

def counter(func):                  #基于redis实现阅读计数，独立IP计数
    def wrap(request):
        aid = int(request.GET.get('aid'))
        redis.incr('ARTICLE-%s-COUNTER' % aid)
        ip = request.META['REMOTE_ADDR']
        if redis.sadd('VIEWER-IP', ip): #添加键值对，对于已存在的为返回0 不做处理，否则为TRUE，去重的意思
            redis.incr('IP-COUNTER')

        return func(request)
    return wrap


