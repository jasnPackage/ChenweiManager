#coding:utf-8
import requests
from common.logger import Log

class Login():
    log = Log()

    def __init__(self,s):
        self.s = s

    def login(self,code,passwd):
        url = "http://192.168.20.100:8081/backend/system/user/login"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
                   "X-Requested-With":"XMLHttpRequest",
                   "Cookie":"JSESSIONID=92D7FB4C7FB917B7D2E8DC429A63443F",
                   "Connection":"keep-alive"
                  }
        d = {"code":code,"passwd":passwd}

        res = self.s.post(url,headers=headers,data=d)
        result1 = res.text #字节输出
        self.log.info(u"调用登录方法，获取结果：%s"%result1)
        return res.json()
