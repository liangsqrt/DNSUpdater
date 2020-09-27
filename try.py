from ip_updater.ipify import Updater
from dns_updater.aliyun import AliDNS


updater = Updater()
updater.run()

# dns = AliDNS()
# dns.run("123.123.123.123")
