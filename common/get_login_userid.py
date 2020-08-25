#coding:utf-8
import requests,json
from config import readConfig

# pda登录接口返回userid

login_data = {
    'loginName':readConfig.loginName,
    'password':readConfig.password
}


url = "http://" + readConfig.test_ip + ":" + readConfig.test_port + "/pdaLogin"

header = {"Content-Type":"application/x-www-form-urlencoded"}

def get_login_userid():
    r = requests.post(url,headers=header,data=login_data)
    userid = r.json()['userId']
    return userid

