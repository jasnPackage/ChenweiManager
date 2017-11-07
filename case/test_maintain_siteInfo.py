#coding:utf-8
import unittest
import requests
from common.logger import Log
from common.mysql_pub import MysqlUtil
from config import readConfig

class Maintain_siteinfo(unittest.TestCase):
    u'''
    站长站点信息接口
    '''
    log = Log()
    mysqlutil = MysqlUtil()
    log.info("---站长站点信息接口测试---")

    def siteinfo(self,userCode):
        '''一个参数：
        登录用户code（工号）：userCode
        '''

        ip = readConfig.ip
        i_port = readConfig.i_port

        url = "http://" + ip + ":" + i_port + "/backend/capacity/maintain/siteInfo"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive"
                 }
        par = {"userCode":userCode}
        r = requests.get(url,params=par)
        result = r.json()
        self.log.info("---站长站点信息接口响应：%s"%result)

        sql = "SELECT CODE FROM cap_courier WHERE CODE IS NOT NULL AND CODE <> '' GROUP BY CODE;"
        userCodes = self.mysqlutil.mysql_getrows(sql)
        s_userCodes = userCodes.__str__()
        if userCode in s_userCodes and userCode != '':
            self.assertEqual(result["code"], '0000')
            self.assertEqual(result["msg"], '接口正常')
            sql1 = "SELECT co.org_name FROM cap_organization co LEFT JOIN cap_courier cc ON co.`org_code` = cc.`org_code` WHERE cc.code = '%s';"%userCode
            orgname = self.mysqlutil.mysql_getrows(sql1)[0][0]
            self.assertEqual(result["data"]["orgName"],orgname)
        elif userCode == '':
            self.assertEqual(result["code"], '0025')
            self.assertEqual(result["msg"], '参数不能为空')
            self.assertEqual(result["data"], {})
        elif userCode != '' and userCode not in s_userCodes:
            self.assertEqual(result["code"], '0000')
            self.assertEqual(result["msg"], '接口正常')
            self.assertEqual(result["data"], None)


    def test_siteinfo1(self):
        u'''测试站长站点信息接口：请求参数正确'''
        self.log.info("---1.请求参数正确：start!---")
        userCode = 'CB00006447'
        self.siteinfo(userCode)
        self.log.info("---pass---")
        self.log.info("")

    def test_siteinfo2(self):
        u'''测试站长站点信息接口：登录用户code（工号）不存在'''
        self.log.info("---2.userCode传入不存在：start!---")
        userCode = 'abc'
        self.siteinfo(userCode)
        self.log.info("---pass---")
        self.log.info("")

    def test_siteinfo3(self):
        u'''测试站长站点信息接口：userCode传入为空'''
        self.log.info("---3.userCode传入为空：start!---")
        userCode = ''
        self.siteinfo(userCode)
        self.log.info("---pass---")
        self.log.info("")

    if __name__ == "__main__":
        unittest.main()