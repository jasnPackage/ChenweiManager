#coding:utf-8
import unittest
import requests
from common.logger import Log
from common.mysql_pub import MysqlUtil
from config import readConfig

class Maintain_list(unittest.TestCase):
    u'''
    站点运力列表接口
    '''
    log = Log()
    mysqlutil = MysqlUtil()
    log.info("---站点运力列表接口测试---")
    def list(self,beginTime,endTime,siteId):
        '''三个参数：
        开始时间：beginTime，结束时间：endTime，站点id：siteId
        '''
        ip = readConfig.ip
        i_port = readConfig.i_port

        url = "http://" + ip + ":" + i_port + "/backend/capacity/maintain/list"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive"
                 }
        par = {"beginTime":beginTime,"endTime":endTime,"siteId":siteId}
        r = requests.get(url,params=par)
        result = r.json()
        self.log.info("---站点运力列表接口响应：%s"%result)
        sql = "SELECT site_id FROM cap_site_detail GROUP BY site_id;"
        siteids = self.mysqlutil.mysql_getrows(sql)
        s_siteids = siteids.__str__()

        if siteId in s_siteids and beginTime < endTime and beginTime != '' and endTime != '' and siteId != '':
            self.assertEqual(result["code"], '0000')
            self.assertEqual(result["msg"], '接口正常')
            sql1 = "SELECT * FROM cap_site_detail WHERE site_id IN (%s) AND site_date >= '%s' AND site_date <= '%s';"%(siteId,beginTime,endTime)
            query_count = self.mysqlutil.mysql_getcounts(sql1)
            self.assertEqual(len(result["data"]), query_count)
        elif beginTime > endTime and beginTime != '' and endTime != '':
            self.assertEqual(result["code"], '0000')
            self.assertEqual(result["msg"], '接口正常')
            sql2 = "SELECT * FROM cap_site_detail WHERE site_id IN (%s) AND site_date >= '%s' AND site_date <= '%s';" % (
            siteId, beginTime, endTime)
            query_count = self.mysqlutil.mysql_getcounts(sql2)
            self.assertEqual(len(result["data"]), query_count)
        elif beginTime == '' or endTime == '' or siteId == '':
            self.assertEqual(result["code"], '0025')
            self.assertEqual(result["msg"], '参数不能为空')
            self.assertEqual((result["data"]), {})


    def test_list1(self):
        u'''测试站点运力列表接口：请求参数正确'''
        self.log.info("---1.请求参数正确：start!---")
        beginTime = '2017-08-25'
        endTime = '2017-08-31'
        siteId = '22'
        self.list(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_list2(self):
        u'''测试站点运力列表接口：beginTime大于endTime'''
        self.log.info("---2.beginTime大于endTime：start!---")
        beginTime = '2017-08-31'
        endTime = '2017-08-25'
        siteId = '22'
        self.list(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_list3(self):
        u'''测试站点运力列表接口：beginTime传入为空'''
        self.log.info("---3.beginTime传入为空：start!---")
        beginTime = ''
        endTime = '2017-08-31'
        siteId = '22'
        self.list(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_list4(self):
        u'''测试站点运力列表接口：endTime传入为空'''
        self.log.info("---4.endTime传入为空：start!---")
        beginTime = '2017-08-25'
        endTime = ''
        siteId = '22'
        self.list(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_list5(self):
        u'''测试站点运力列表接口：siteId传入为空'''
        self.log.info("---5.siteId传入为空：start!---")
        beginTime = '2017-08-25'
        endTime = '2017-08-31'
        siteId = ''
        self.list(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_list6(self):
        u'''测试站点运力列表接口：beginTime,endTime和siteId传入为空'''
        self.log.info("---6.beginTime,endTime和siteId传入为空：start!---")
        beginTime = ''
        endTime = ''
        siteId = ''
        self.list(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")


if __name__ == "__main__":
    unittest.main()
