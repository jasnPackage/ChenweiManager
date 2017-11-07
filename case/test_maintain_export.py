#coding:utf-8
import unittest
import requests
from common.logger import Log
from common.mysql_pub import MysqlUtil
from config import readConfig

class Maintain_export(unittest.TestCase):
    u'''
    站点运力列表导出接口
    '''
    log = Log()
    mysqlutil = MysqlUtil()
    log.info("---站点运力列表导出接口测试---")
    def export(self,beginTime,endTime,siteId):
        '''三个参数：
        开始时间：beginTime，结束时间：endTime，站点id：siteId
        '''
        ip = readConfig.ip
        i_port = readConfig.i_port

        url = "http://" + ip + ":" + i_port + "/backend/capacity/maintain/export"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive"
                 }
        par = {"beginTime":beginTime,"endTime":endTime,"siteId":siteId}
        r = requests.get(url,params=par)
        result_head = r.headers
        self.log.info("---站点运力列表导出接口响应头：%s"%result_head)
        sql = "SELECT site_id FROM cap_site_detail GROUP BY site_id;"
        siteids = self.mysqlutil.mysql_getrows(sql)
        s_siteids = siteids.__str__()

        if siteId in s_siteids and beginTime < endTime and beginTime != '' and endTime != '' and siteId != '':
            self.assertIn('.xls',result_head['Content-Disposition'])
        elif beginTime > endTime and beginTime != '' and endTime != '':
            result_body = r.json()
            self.log.info("---站点运力列表导出接口响应：%s" % result_body)
            self.assertEqual(result_body["code"], '0026')
            self.assertEqual(result_body["msg"], '未查询到数据')
            sql2 = "SELECT * FROM cap_site_detail WHERE site_id IN (%s) AND site_date >= '%s' AND site_date <= '%s';" % (
            siteId, beginTime, endTime)
            query_count = self.mysqlutil.mysql_getcounts(sql2)
            self.assertEqual(len(result_body["data"]), query_count)
            self.assertEqual(result_body["data"], {})
        elif beginTime == '' or endTime == '' or siteId == '':
            result_body = r.json()
            self.log.info("---站点运力列表导出接口响应：%s" % result_body)
            self.assertEqual(result_body["code"], '0025')
            self.assertEqual(result_body["msg"], '参数不能为空')
            self.assertEqual((result_body["data"]), {})


    def test_export1(self):
        u'''测试站点运力列表导出接口：请求参数正确'''
        self.log.info("---1.请求参数正确：start!---")
        beginTime = '2017-08-25'
        endTime = '2017-08-31'
        siteId = '22'
        self.export(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_export2(self):
        u'''测试站点运力列表导出接口：beginTime大于endTime'''
        self.log.info("---2.beginTime大于endTime：start!---")
        beginTime = '2017-08-31'
        endTime = '2017-08-25'
        siteId = '22'
        self.export(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_export3(self):
        u'''测试站点运力列表导出接口：beginTime传入为空'''
        self.log.info("---3.beginTime传入为空：start!---")
        beginTime = ''
        endTime = '2017-08-31'
        siteId = '22'
        self.export(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_export4(self):
        u'''测试站点运力列表导出接口：endTime传入为空'''
        self.log.info("---4.endTime传入为空：start!---")
        beginTime = '2017-08-25'
        endTime = ''
        siteId = '22'
        self.export(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_export5(self):
        u'''测试站点运力列表导出接口：siteId传入为空'''
        self.log.info("---5.siteId传入为空：start!---")
        beginTime = '2017-08-25'
        endTime = '2017-08-31'
        siteId = ''
        self.export(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")

    def test_export6(self):
        u'''测试站点运力列表导出接口：beginTime,endTime和siteId传入为空'''
        self.log.info("---6.beginTime,endTime和siteId传入为空：start!---")
        beginTime = ''
        endTime = ''
        siteId = ''
        self.export(beginTime,endTime,siteId)
        self.log.info("---pass---")
        self.log.info("")


if __name__ == "__main__":
    unittest.main()
