import socket
import time
from logger import GlobalLogger
from config import *
import requests


class Updater(object):
    def __init__(self):
        self.name = "ipify_updater"
        self.logger = GlobalLogger(logger_name=self.name)
        self.ip_file = os.path.join(dir_source, "ipify")
        self.ip = ""
        try:
            with open(self.ip_file, "r") as fl:
                self.ip = fl.read()
        except Exception as e:
            self.logger.warning(e)
            self.logger.info("创建ip文件 ——> "+self.ip_file)
            with open(self.ip_file, "w") as fl:
                fl.write(self.ip)

    def update_ip(self, ip):
        if ip != self.ip:
            self.logger.info("ip 已经发生改变, old value: {}, new_value:{}".format(self.ip, ip))
            self.ip = ip
            with open(self.ip_file, "w") as fl:
                fl.write(self.ip)

    def run(self):
        try:
            ip_str = requests.get(url="https://api.ipify.org/?format=json", timeout=2).json()['ip']
            self.update_ip(ip_str)
        except Exception as e:
            print(e)
