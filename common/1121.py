# #!/usr/bin/python
# # coding=utf8
# # Name:  py_sendattach.py
# # Purpose:       send ptp data to antifraud
# # Author:        yangshuqiang
#
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import smtplib
# import os, sys
#
# mail_host = 'smtp.163.com'
# mail_from = 'amazinglala@163.com'
# mail_pass = '40711960556123'
#
#
# def addAttch(to_list, subject, content, path):
#     # msg = MIMEMultipart('related')  ##采用related定义内嵌资源的邮件体
#     msg = MIMEMultipart()
#     msgtext = MIMEText(content, _subtype='html', _charset='utf-8')  ##_subtype有plain,html等格式，避免使用错误
#
#     msg.attach(msgtext)
#
#     os.chdir(path)
#     dir = os.getcwd()
#
#     for fn in os.listdir(dir):  ##返回字符串文件名
#         print(fn)
#         attach = MIMEText(open(fn, 'rb').read(), "base64", "utf-8")
#         attach["Content-Type"] = 'application/octet-stream'
#         attach["Content-Disposition"] = 'attachment; filename=' + fn
#         msg.attach(attach)
#     msg['Subject'] = subject
#     msg['From'] = mail_from
#     msg['To'] = to_list
#     return msg
#
#
# def sendMail(msg):
#     try:
#         server = smtplib.SMTP()
#         server.connect(mail_host, 25)
#         server.starttls()
#         server.login(mail_from, mail_pass)
#         server.sendmail(mail_from, msg['To'], msg.as_string())
#         server.quit()  ##断开smtp连接
#         print("邮件发送成功")
#     except Exception as e:
#         print("失败" + str(e))
#
#
# if __name__ == '__main__':
#     msg = addAttch('wuxia1@3856.cc', '对账', '对账数据', r'C:\\Users\\Administrator\\PycharmProjects\\zhandian_jiekou\\report1')
#     sendMail(msg)


# a = r"C:\Users\Administrator\PycharmProjects\zhandian_jiekou\report\2017_10_10_18_11_59result.html"
# b = a.split('report\\')
# print(b[1])

# import xlrd
# data = xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\1.xlsx')
# table = data.sheet_by_index(1)
# nrows = table.nrows
# print(table.cell_value(1,0))

# for i in range(nrows):
#     print(table.row_values(i))
#
# for i in range(1,5):
#     for j in range(0,3):
#         print(i,j)


# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Sex': 'female'}
#
# dict.update(dict2)
# print(dict)
# dict3 = {'Sex1': 'female1'}
#
# dict.update(dict3)
# print(dict)


# import hashlib
# import random
# import string

# def gen_random_string(str_len):
#     chars = string.ascii_letters + string.digits
#     s = [random.choice(chars) for s in range(4)]
#     print(''.join(s))


# def gen_random_string(str_len):
#     print(
#      ''.join(
#         random.choice(string.ascii_letters + string.digits) for _ in range(str_len)
#     )
#     )
#
# def gen_md5(*args):
#     print(hashlib.md5("".join(args).encode('utf-8')).hexdigest())
#
#
# gen_random_string(4)
#
# TOKEN = "debugtalk"
# data = '{"name": "user", "password": "123456"}'
# random = "A2dEx"
# gen_md5(TOKEN, data, random)


# from xlutils.copy import copy
# import xlrd
#
# rd = xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\站点运力列表.xls')
#
# wb = copy(rd)
#
# ws = wb.get_sheet(1)
# ws.write(1,5,'pass')
# wb.save(r'C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\站点运力列表.xls')


# -*- coding: utf-8 -*-
# '''
# Created on 2012-12-17
#
# @author: walfred
# @module: XLRDPkg.write_append
# @description:
# '''
# import os
# from xlutils.copy import copy
# import xlrd as ExcelRead
#
#
# def write_append(file_name):
#     values = ["Ann", "woman", 22, "UK"]
#
#     r_xls = ExcelRead.open_workbook(file_name)
#     r_sheet = r_xls.sheet_by_index(0)
#     rows = r_sheet.nrows
#     w_xls = copy(r_xls)
#     sheet_write = w_xls.get_sheet(0)
#
#     for i in range(0, len(values)):
#         sheet_write.write(i, rows, values[i])
#
#     w_xls.save(file_name);
#
#
# if __name__ == "__main__":
#     write_append(r"C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\test_append.xls")


# #coding:utf-8
#
# import xlrd,os
# import requests
# import openpyxl
# from openpyxl.styles import Font
# # from xlutils.copy import copy
# from datetime import datetime
# from xlrd import xldate_as_tuple
# from config import readConfig
# from common.logger import Log
# from case.user_login import Login
#
#
#
# runmode = readConfig.runmode
#
# if runmode == 'test':
#     ip = readConfig.test_ip  # 获取配置文件中接口ip
#     i_port = readConfig.test_port  # 获取配置文件中接口port
# elif runmode == 'pro':
#     ip = readConfig.pro_ip  # 获取配置文件中接口ip
#     i_port = readConfig.pro_port  # 获取配置文件中接口port
# else:
#     raise ValueError("run_config.ini文件配置的运行模式错误")

# import openpyxl
#
#
# wb = openpyxl.load_workbook(r"C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\a1.xlsx")
# ws = wb.worksheets[0]
# ws.cell(row=1,column=3,value='aaaa')
# wb.save(r"C:\Users\Administrator\PycharmProjects\zhandian_jiekou\data\a1.xlsx")

# from datetime import datetime
# from time import sleep
# a = datetime.now()
# print(a)
# sleep(1)
# b = datetime.now()
# print(b)
# print((b-a).seconds)


# import hashlib
# import base64
#
# md5 = hashlib.md5()
#
#
# # a = "<request><waybills><waybill><receiver><receiverName>张三</receiverName><receiverMobile>13000000000</receiverMobile><receiverZip>431400</receiverZip><receiverProvince>甘肃省</receiverProvince><receiverCity>兰州市</receiverCity><receiverArea>新洲区</receiverArea><receiverDistrict>李集街道</receiverDistrict><receiverAddress>天水南路222号</receiverAddress></receiver><sender><shopName>天猫超市</shopName><senderName>天猫超市仓库</senderName><senderPhone>02781739210</senderPhone><senderZip>430208</senderZip><senderProvince>甘肃省</senderProvince><senderCity>兰州市</senderCity><senderArea>新洲区</senderArea><senderAddress>金口街旭光村菜鸟物流园3号库</senderAddress></sender><packageInfo><packageCode>test0926001</packageCode><isExpensive>false</isExpensive><weight>2302</weight><volume>7888000</volume><length>290</length><width>170</width><height>160</height><storeOutTime>2017-09-22 08:55:04</storeOutTime></packageInfo><carrier/><sortingInfo><routetype>1</routetype><storeCode>pressureTest</storeCode><deliveryCode>CHENGBANGPEISONG-0001</deliveryCode><deliveryWlbCode>NJCB-001</deliveryWlbCode><cpSimplyCode>C</cpSimplyCode><citySimplyCode>H1</citySimplyCode><routePath>{'nextRouteId':890,'nextRouteType':2,'targerRdcType':2,'targetRdcId':890}</routePath><siteId>4859</siteId><siteCode>1619095</siteCode><carrierCode>CBWL</carrierCode><sortingRequireTimes><requireSendTime>2017-09-24 23:59:00</requireSendTime></sortingRequireTimes><sortingService><expressSerType>108</expressSerType></sortingService></sortingInfo><order><lgOrderSource>WLB</lgOrderSource><storeOrderCode>ydhtest1341573</storeOrderCode><logisticsId>LP00079477100697</logisticsId><mailNo>ddhtest5454253</mailNo><customerCode>SB-ZFB</customerCode><deliveryType>1</deliveryType><distributionType>1</distributionType></order><deliveryNodeInfo><nodeCode>1619095</nodeCode><nodeName>晟邦湖北分拨中心</nodeName><deliveryStatus>MainWaybillAccess</deliveryStatus><firstOwnerRdcCode>1619095</firstOwnerRdcCode></deliveryNodeInfo><uniqueCode>MainWaybillAccesstest09260012017-09-22 09:13:11</uniqueCode><remark>zpb_chuyan_cb</remark></waybill></waybills></request>"
# # b = a.replace("\\>\\s+\\<", "><")+"alogalog"
# #
# #
# # md5.update(b.encode('utf-8'))
# # b = md5.digest()
# # print(u"16位md5加密结果：%s"% b)
# # print(u"16位md5加密结果再进行base64编码：%s" % base64.b64encode(b).decode('utf-8'))
#
# c = "1508465162269"+"kfzc@1234"
# md5.update(c.encode('utf-8'))
# d = md5.hexdigest()
# print(d)

# import string
# print(string.ascii_uppercase[0:7])
# for i in string.ascii_uppercase[0:7]:
#     print(i)

# sum = 1
# for i in range(0,101):
#     # sum = sum + i
#     sum += i
#
# print(sum)

# a = [str(i) for i in range(0,10) if i%2==0]
# print(''.join(a))

# print(i for i in range(0,10))



# a = [1,2]
#
# print("-".join(a))

# a = []
# for i in range(0,10):
#     if i%2 == 0:
#         a.append(str(i))
# print("".join(a))



# a = []
# for n in range(1,21):
#     if n <= 3:
#         for i in range(1,6):
#             a.append(i)
#         print(a)


    # for i in range(n,n+5):
    #     if i == n:
    #         a.append(str(i)+'*')
    #     else:
    #         a.append(i)
    # print(str(n)+' '+str(a))

# import random
#
# a = [1, 2, 3, 4, 5,6]
# random.shuffle(a)
#
# b = sorted(a,reverse=True)
# print(list(zip(a,b)))

# b = a[1::2]
# print(b)
#
# # print(b)
# sum = 0
# for i in b:
#     sum = (i+3) + sum
# print(sum)

# a = 'abcdef'
# print(''.join(sorted(a,reverse=True)))
# print(sorted(a,reverse=True))
# for i in sorted(a,reverse=True):
#     print(''.join(i))
# b = ['a','b','c']
# print(''.join(b))

# x = y = z = 1
# import re

# s = "abbacd"
#
# b = list(s)
# b1 = list(set(b))
# b1.sort(key=b.index)
# print(b1)
#
# c = {}
# for i in b1:
#     if s.count(i) == 1:
#         c[i] = s.count(i)
#         break
# for j in c.keys():
#     print(j)

# for i in b:
#     if a1.count(i) > 1:
#         print("字符：%s，重复次数：%s"%(i,a1.count(i)))

# def is_odd(n):
#     return n % 2 == 1
#
# newlist = filter(is_odd,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(newlist))


# s = "i am a student"
# print(''.join(list(s[::-1])))

# s1 = 'abcadfga'
# s2 = 'a'
# print(s1.replace(s2,''))

# L1 = [1,2,23,44,51]
#
# a = ''.join(map(str,L1))
# L2 = list(a)
# L2.sort()
# s = ''.join(L2)
# print(s)


# L1 = [1,2,3]
# L2 = [1]
# for i in L1:
#     if i not in L2:
#         print(i)


list = ['a','b','c']
list.insert(0,'1')
print(list)


