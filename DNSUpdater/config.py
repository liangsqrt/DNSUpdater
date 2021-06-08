import os, sys
import json


# 基本配置
ip_update_interval = 1
source_path_name = "source"
log_path_name = "log"
dir_base = os.path.dirname(os.path.abspath(__file__))
dir_source = os.path.join(dir_base, source_path_name)
dir_log = os.path.join(dir_base, log_path_name)


# 阿里云配置
ipv4_flag = 1
accessKeyId = ""  # 将accessKeyId改成自己的accessKeyId
accessSecret = ""  # 将accessSecret改成自己的accessSecret
domain = ""  # 你的主域名
name_ipv4 = ""  # 要进行ipv4 ddns解析的子域名

ip_udpater = "dnspod"

# 环境配置
if not os.path.exists(dir_source):
    os.mkdir(dir_source)
if not os.path.exists(dir_log):
    os.mkdir(dir_log)

