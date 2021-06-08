# from IpUpdater.ipify import IpifyUpdaterUpdater
# from IpUpdater.dnspod import DnspodUpdater
# from DNSUpdater.aliyun import AliDNS
from DNSUpdater.updater import Runner

updater = Runner()
updater.run()

# dns = AliDNS()
# dns.run("123.123.123.123")
