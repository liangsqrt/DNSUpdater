# from ip_updater.ipify import IpifyUpdaterUpdater
# from ip_updater.dnspod import DnspodUpdater
# from dns_updater.aliyun import AliDNS
from updater import Runner

updater = Runner()
updater.run()

# dns = AliDNS()
# dns.run("123.123.123.123")
