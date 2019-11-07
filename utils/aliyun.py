#!/usr/bin/env python
# coding=utf-8
from random import Random
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from users.models import MobileVerify 


class Aliyun():
    def __init__(self, keyid, secret):
        self.accessKeyId = keyid
        self.accessSecret = secret

    def send_sms(self, mobile, code):
        client = AcsClient(self.accessKeyId, self.accessSecret, 'cn-hangzhou')
        json_code = {"code": code}
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')
        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', mobile)
        request.add_query_param('SignName', "航天创客")
        request.add_query_param('TemplateCode', "SMS_175539342")
        request.add_query_param('TemplateParam', str(json_code))
        response = client.do_action_with_exception(request)
        return str(response, encoding = 'utf-8')

def random_str(random_length=6):
    str = ''
    # 生成字符串的可选字符串
    chars = '1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str

def send_code(mobile):
    code = random_str(6)
    mobileverify = MobileVerify()
    mobileverify.mobile = mobile
    mobileverify.code = code
    keyid = "LTAI4FcUXAWPquTQDFYzwguF"
    secret = "PUgtPYgNjtaVvsQBbnpPCRHOlYX1TB"
    ali = Aliyun(keyid, secret)
    sms_status = ali.send_sms(mobile, code)
    if (eval(sms_status)["Message"]) == 'OK':
        mobileverify.save()
    return sms_status
    # print(eval(sms_status)["Message"])



if __name__ == '__main__':
    keyid = "LTAI4FcUXAWPquTQDFYzwguF"
    secret = "PUgtPYgNjtaVvsQBbnpPCRHOlYX1TB"
    send_code('13121265866')
