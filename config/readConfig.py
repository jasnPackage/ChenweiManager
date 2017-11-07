# coding:utf-8
import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "cfg.ini")
conf = configparser.ConfigParser()
conf.read(configPath,encoding='utf-8')

'''
读取邮箱和接口地址信息
'''

smtp_server = conf.get("email", "smtp_server")

sender = conf.get("email", "sender")

psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver")

port = conf.get("email", "port")

test_ip = conf.get("test_interface","ip")

test_port = conf.get("test_interface","port")

pro_ip = conf.get("pro_interface","ip")

pro_port = conf.get("pro_interface","port")


'''
读取运行配置信息
'''
configPath_1 = os.path.join(cur_path,"run_config.ini")
conf_1 = configparser.ConfigParser()
conf_1.read(configPath_1,encoding='utf-8')

runmode = conf_1.get("runconfig","runmode")

pro_name = conf_1.get("testreport","pro_name")
pro_version = conf_1.get("testreport","pro_version")
tice_time = conf_1.get("testreport","tice_time")
tice_person = conf_1.get("testreport","tice_person")
tester = conf_1.get("testreport","tester")
test_time = conf_1.get("testreport","test_time")
auditor = conf_1.get("testreport","auditor")
pass_case = conf_1.get("testreport","pass_case")
fail_case = conf_1.get("testreport","fail_case")
success_rate = conf_1.get("testreport","success_rate")






