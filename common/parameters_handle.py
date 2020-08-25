#coding:utf-8
import re
from common import logger
from common import get_login_userid

class TestData:
    """这个类的作用：专门用来保存一些要替换的数据"""

    userId = get_login_userid.get_login_userid()
    pass



# def parameters_handle(data,partten=r"\${(.*?)}",*args):
#     '''根据正则匹配参数化，需要替换的参数'''

    # # 判断是否有需要替换多个的数据
    # while re.findall(partten,data):
    #     # 匹配出所有要替换的数据
    #     res = re.findall(partten,data)
    #     new_res = ['${' + x + '}' for x in res]
    #     print(new_res)
    #     #提取待替换的内容
    #     for i in range(len(new_res)):
    #         data = data.replace(new_res[i],args[i])
    #     #item = res.group()
    #     #获取替换内容中的数据项
    #     # data = data.replace(item,field)
    #
    # return data


def parameters_handle(data,partten=r"\${(.*?)}"):
    # 判断是否有需要替换一个的数据
    while re.search(partten,data):
        # 匹配出所有要替换的数据
        res = re.search(partten, data)
        # 提取待替换的内容
        item = res.group()
        # 获取替换内容中的数据项
        data = data.replace(item,TestData.userId)

    return data



data = '{"pass_word":"abcd1","new_pass_word":"123456","id":"${userId}"}'
a = parameters_handle(data)
print(a)





# data = '{"pass_word":"abcd1","new_pass_word":"123456","id":"${userId}"}'
# partten=r"\${(.*?)}"
# res = re.search(partten,data)
# a = res.group()
# b = data.replace(a,'admin')
# print(b)
