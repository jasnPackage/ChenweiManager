#coding:utf-8
import unittest
import requests
from common.logger import Log
from common.mysql_pub import MysqlUtil
from config import readConfig

class Maintain_siteCapacityInfo(unittest.TestCase):
    u'''
    获取站点运力数据接口
    '''
    log = Log()
    mysqlutil = MysqlUtil()
    log.info("---获取站点运力数据接口测试---")

    def siteCapacityInfo(self,siteDetailId):
        '''一个参数：
        siteDetailId：string
        '''
        ip = readConfig.ip
        i_port = readConfig.i_port

        url = "http://" + ip + ":" + i_port + "/backend/capacity/maintain/siteCapacityInfo"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive"
                 }
        par = {"siteDetailId":siteDetailId}
        r = requests.get(url,params=par)
        result = r.json()
        self.log.info("---获取站点运力数据接口响应：%s"%result)
        sql = "SELECT id FROM cap_site_detail WHERE id IS NOT NULL AND id <> '' GROUP BY id;"
        siteDetailIds = self.mysqlutil.mysql_getrows(sql)
        s_siteDetailIds = siteDetailIds.__str__()
        if siteDetailId in s_siteDetailIds and siteDetailId != '':
            self.assertEqual(result["code"], '0000')
            self.assertEqual(result["msg"], '接口正常')
            sql1 = "SELECT org_name FROM cap_organization WHERE org_code IN (SELECT site_id FROM cap_site_detail WHERE id IN ( %s ));"%siteDetailId
            sitename = self.mysqlutil.mysql_getrows(sql1)[0][0]
            self.assertEqual(result["data"]["siteName"],sitename)
        elif siteDetailId == '':
            self.assertEqual(result["code"], '0025')
            self.assertEqual(result["msg"], '参数不能为空')
            self.assertEqual(result["data"], {})
        elif siteDetailId != '' and siteDetailId not in s_siteDetailIds:
            self.assertEqual(result["code"], '0000')
            self.assertEqual(result["msg"], '接口正常')
            self.assertEqual(result["data"], None)


    def test_siteinfo1(self):
        u'''测试获取站点运力数据接口：请求参数正确'''
        self.log.info("---1.请求参数正确：start!---")
        siteDetailId = '10'
        sql2 = ""
        self.siteCapacityInfo(siteDetailId)
        self.log.info("---pass---")
        self.log.info("")

    def test_siteinfo2(self):
        u'''测试获取站点运力数据接口：siteDetailId不存在'''
        self.log.info("---2.siteDetailId传入不存在：start!---")
        siteDetailId = 'abc'
        self.siteCapacityInfo(siteDetailId)
        self.log.info("---pass---")
        self.log.info("")

    def test_siteinfo3(self):
        u'''测试获取站点运力数据接口：siteDetailId传入为空'''
        self.log.info("---3.siteDetailId传入为空：start!---")
        siteDetailId = ''
        self.siteCapacityInfo(siteDetailId)
        self.log.info("---pass---")
        self.log.info("")

    if __name__ == "__main__":
        unittest.main()