import os
import socket
from tornado.tcpserver import TCPServer
from tornado.httpserver import HTTPServer

__version__ = '1.0.1'

SYSTEMD_SOCKET_FD = 3  # Magic number !


class SystemdMixin(object):
    @property
    def systemd(self):
        return os.environ.get('LISTEN_PID', None) == str(os.getpid())

    def listen(self, port, address='', backlog=128, family=None, type=None):
        if self.systemd:
            self.request_callback.systemd = True
            # Systemd activated socket
            family = family or (
                socket.AF_INET6 if socket.has_ipv6 else socket.AF_INET)
            type = type or socket.SOCK_STREAM
            sck = socket.fromfd(SYSTEMD_SOCKET_FD, family, type)
            self.add_socket(sck)
            sck.setblocking(0)
            sck.listen(128)
        else:
            self.request_callback.systemd = False
            super(SystemdMixin, self).listen(port, address)


class SystemdTCPServer(SystemdMixin, TCPServer):
    pass


class SystemdHTTPServer(SystemdMixin, HTTPServer):
    pass
