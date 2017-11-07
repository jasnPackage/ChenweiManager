#coding:utf-8
import unittest
import requests
from case.user_login import Login
from common.logger import Log
from common.mysql_pub import MysqlUtil
from config import readConfig

class Capsummary_update(unittest.TestCase):
    u'''
    站点运力修改
    '''

    s = requests.session()
    lon = Login(s)
    log = Log()
    mysqlutil = MysqlUtil()
    log.info("---站点运力修改接口测试---")

    def update(self,datas):
        '''一个参数
        datas
        :param datas:
        :return:
        '''
        ip = readConfig.ip
        i_port = readConfig.i_port

        url = "http://" + ip + ":" + i_port + "/backend/capacity/capsummary/update"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
        }

        code = "xuxingan"
        passwd = "admin"
        self.lon.login(code,passwd)
        d = {"datas":datas}
        r = self.s.post(url,data=d,headers=headers)
        result = r.json()
        print(result)

        sql = " SELECT id FROM cap_delivery_detail  GROUP BY id;"
        ids = self.mysqlutil.mysql_getrows(sql)
        s_ids = ids.__str__()
        if datas != '':
            for i in datas.split(','):
                if i.split('&')[0] in s_ids:
                    self.assertEqual(result["code"], '0000')
                    self.assertEqual(result["msg"], '接口正常')
                    self.assertEqual(result["data"], [])
                elif i.split('&')[0] not in s_ids:
                    self.assertEqual(result["code"], '9999')
                    self.assertEqual(result["msg"], '未知异常')
                    self.assertEqual(result["data"], {})
        elif datas == '':
            self.assertEqual(result["code"], '0025')
            self.assertEqual(result["msg"], '参数不能为空')
            self.assertEqual(result["data"], {})


    def test_update1(self):
        u'''测试站点运力修改接口：修改一条记录'''
        self.log.info("---1.修改一条记录：start!---")
        datas = '6&10'
        self.update(datas)
        self.log.info("---pass---")
        self.log.info("")

    def test_update2(self):
        u'''测试站点运力修改接口：批量修改多条记录'''
        self.log.info("---2.批量修改多条记录：start!---")
        datas = '6&10,8&20,10&0'
        self.update(datas)
        self.log.info("---pass---")
        self.log.info("")

    def test_update3(self):
        u'''测试站点运力修改接口：批量修改多条记录'''
        self.log.info("---3.datas传入为空：start!---")
        datas = ''
        self.update(datas)
        self.log.info("---pass---")
        self.log.info("")





if __name__ == "__main__":
    unittest.main()