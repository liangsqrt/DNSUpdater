from DNSUpdater.DNSUpdater.aliyun import *
from DNSUpdater.IpUpdater.dnspod import *


class Runner():
    def __init__(self, update_interval=None):
        if ip_udpater == "dnspod":
            self.ip_updater = DnspodUpdater()
        elif ip_udpater == "ipify":
            self.ip_updater = IpifyUpdater()
        if update_interval:
            self.interval = update_interval
        else:
            self.interval = ip_update_interval
        self.dns_updater = AliDNS()

    def run(self):
        while True:
            if self.ip_updater.run():
                self.dns_updater.run(self.ip_updater.ip)
            time.sleep(self.interval)

