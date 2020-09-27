import socket
import time
from logger import GlobalLogger
from config import *


class DnspodUpdater(object):
    def __init__(self):
        self.name = "dnspod_updater"
        self.logger = GlobalLogger(logger_name=self.name)
        self.ip_file = os.path.join(dir_source, "dnspod")
        self.ip = ""
        try:
            with open(self.ip_file, "r") as fl:
                self.ip = fl.read()
        except Exception as e:
            self.logger.warning(e)
            self.logger.info("创建ip文件 ——> "+self.ip_file)
            with open(self.ip_file, "w+") as fl:
                fl.write(self.ip)

    def update_ip(self, ip):
        if ip != self.ip:
            self.logger.info("ip 已经发生改变, old value: {}, new_value:{}".format(self.ip, ip))
            self.ip = ip
            with open(self.ip_file, "w") as fl:
                fl.write(self.ip)
            return True
        else:
            return False

    def run(self):
        try:
            sock = socket.create_connection(('ns1.dnspod.net', 6666), timeout=2)
            ip_bin = sock.recv(1024)
            sock.close()
            ip_str = ip_bin.decode("utf-8")
            return self.update_ip(ip_str)
        except Exception as e:
            print(e)
