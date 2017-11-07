#coding:utf-8
import unittest
import requests
import random
from common.logger import Log
from common.mysql_pub import MysqlUtil
from config import readConfig

class Common_sites(unittest.TestCase):
    u'''
    站点列表接口
    '''
    log = Log()
    mysqlutil = MysqlUtil()
    log.info("---站点列表接口测试---")

    def sites(self,cityCompanyCode):
        '''一个参数
        市公司编码：cityCompanyCode
        :param cityCompanyCode:
        :return:
        '''
        ip = readConfig.ip
        i_port = readConfig.i_port

        url = "http://" + ip + ":" + i_port + "/backend/capacity/common/sites"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
        }
        d = {"cityCompanyCode":cityCompanyCode}
        r = requests.post(url,data=d,headers=headers)
        result = r.json()

        self.log.info("---获取响应结果：%s" % result)
        # self.log.info("---校验code字段---")
        self.assertEqual(result["code"], '0000')

        # self.log.info("---校验msg字段---")
        self.assertEqual(result["msg"], '接口正常')

        sql1 = "SELECT parent_code FROM cap_organization  WHERE LEVEL = '3' GROUP BY parent_code;"
        cityCompanyCodes = self.mysqlutil.mysql_getrows(sql1)  #从数据库中取出所有的市公司编码（parent_code）
        s_cityComcityCompanyCodes = cityCompanyCodes.__str__() #将元组转换成字符串
        # a_city = cityCompanyCodes[random.randint(0,(len(cityCompanyCodes)))][0]

        if cityCompanyCode in s_cityComcityCompanyCodes :
            # self.log.info("---校验data中的查询结果数量---")
            sql = "SELECT * FROM cap_organization WHERE LEVEL = '3' AND parent_code = '%s';" % cityCompanyCode
            counts = self.mysqlutil.mysql_getcounts(sql)
            self.assertEqual(len(result["data"]), counts)
        elif cityCompanyCode == '':
            # self.log.info("---校验data中的查询结果数量---")
            self.assertEqual(result["data"], [])
        elif cityCompanyCode != '' and cityCompanyCode not in s_cityComcityCompanyCodes:
            # self.log.info("---校验data中的查询结果数量---")
            self.assertEqual(result["data"], [])

    def test_sites1(self):
        u'''测试站点列表接口：请求参数正确'''
        self.log.info("---1.请求参数正确：start!---")
        sql1 = "SELECT parent_code FROM cap_organization  WHERE LEVEL = '3' GROUP BY parent_code;"
        cityCompanyCodes = self.mysqlutil.mysql_getrows(sql1)
        print(cityCompanyCodes)
        cityCompanyCode = cityCompanyCodes[random.randint(0,(len(cityCompanyCodes)))][0]
        self.sites(cityCompanyCode)
        self.log.info("---pass---")
        self.log.info("")

    def test_sites2(self):
        u'''测试站点列表接口：cityCompanyCode传入为空'''
        self.log.info("---2.cityCompanyCode传入为空：start!---")
        cityCompanyCode = ""
        self.sites(cityCompanyCode)
        self.log.info("---pass---")
        self.log.info("")

    def test_sites3(self):
        u'''测试站点列表接口：cityCompanyCode传入不存在的市公司编码'''
        self.log.info("---3.cityCompanyCode传入不存在的市公司编码：start!---")
        cityCompanyCode = "a"
        self.sites(cityCompanyCode)
        self.log.info("---pass---")
        self.log.info("")


if __name__ == "__main__":
    unittest.main()