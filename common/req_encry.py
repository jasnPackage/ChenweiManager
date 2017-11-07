#!/usr/bin/python
# coding=utf8

import hashlib
import base64

'''
接口请求加密
'''

def jiami(str,key):

    md5 = hashlib.md5()


    b = str.replace("\\>\\s+\\<", "><")+key


    md5.update(b.encode('utf-8'))
    b = md5.digest()
    c = base64.b64encode(b).decode('utf-8')
    return c
    # print(u"16位md5加密结果：%s"% b)
    # print(u"16位md5加密结果再进行base64编码：%s" % base64.b64encode(b).decode('utf-8'))