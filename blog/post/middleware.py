from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

BLOCKIP = [                     #定义中间件，阻止IP在BLOCKIP里的用户访问----
    # '127.0.0.1',
    '192.168.0.4'
]


class BlockIP(MiddlewareMixin): #要继承
    @staticmethod
    def is_blocked_ip(ip):
        return ip in BLOCKIP

    def process_request(self, request):
        # host = request.get_host()
        # if ':' in host:
        #     host = host.split(':')[0]
        ip = request.META['REMOTE_ADDR']
        if self.is_blocked_ip(ip):
            return render(request, 'blockers.html')
        return
