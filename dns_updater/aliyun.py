from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from aliyunsdkalidns.request.v20150109.DeleteSubDomainRecordsRequest import DeleteSubDomainRecordsRequest
from logger import GlobalLogger
import json
from config import *


client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')


class AliDNS():
    def __init__(self):
        self.name = "ali"
        self.logger = GlobalLogger(logger_name=self.name)

    def update(self, RecordId, RR, Type, Value):  # 修改域名解析记录
        request = UpdateDomainRecordRequest()
        request.set_accept_format('json')
        request.set_RecordId(RecordId)
        request.set_RR(RR)
        request.set_Type(Type)
        request.set_Value(Value)
        response = client.do_action_with_exception(request)
        self.logger.info("修改域名解析记录， 结果是：", response)

    def add(self, DomainName, RR, Type, Value):  # 添加新的域名解析记录
        self.logger.info("添加新的记录: domain:{}, value:{}".format(DomainName, Value))
        from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
        request = AddDomainRecordRequest()
        request.set_accept_format('json')
        request.set_DomainName(DomainName)
        request.set_RR(RR)
        request.set_Type(Type)
        request.set_Value(Value)
        response = client.do_action_with_exception(request)
        self.logger.info("添加域名解析记录， 结果是：", response)

    def run(self, ipv4):
        request = DescribeSubDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_DomainName(domain)
        request.set_SubDomain(name_ipv4 + '.' + domain)
        response = client.do_action_with_exception(request)
        domain_list = json.loads(response)
        self.logger.info("获取到IPv4地址：%s" % ipv4)
        if domain_list['TotalCount'] == 0:
            self.add(domain, name_ipv4, "A", ipv4)
            self.logger.info("新建域名解析成功")
        elif domain_list['TotalCount'] == 1:
            if domain_list['DomainRecords']['Record'][0]['Value'].strip() != ipv4.strip():
                self.update(domain_list['DomainRecords']['Record'][0]['RecordId'], name_ipv4, "A", ipv4)
                self.logger.info("修改域名解析成功")
            else:
                self.logger.info("IPv4地址没变")
        elif domain_list['TotalCount'] > 1:
            self.logger.info("域名记录大于2个")
            request = DeleteSubDomainRecordsRequest()
            request.set_accept_format('json')
            request.set_DomainName(domain)
            request.set_RR(name_ipv4)
            response = client.do_action_with_exception(request)
            self.add(domain, name_ipv4, "A", ipv4)
            self.logger.info("域名记录大于2个，已经删除并重新添加了记录。")
