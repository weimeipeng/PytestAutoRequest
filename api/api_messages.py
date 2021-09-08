# @Time : 2021/9/6 22:18 
# @Author : 韦鹏
# @File : api_messages.py
# @Software: PyCharm


import requests
#加载测试数据
from common.http_requests import HttpRequests
from common.read_yaml import ReadYaml
from api.get_token import Get_Token


class Message(object):
    def get_message(self,token):

        url='http://121.41.14.39:9097/api/messages/1/4'

        HttpRequests().headers['X-AUTH-TOKEN']=token

        resp = requests.get(url,headers=HttpRequests().headers)
        return resp

    def push_message(self,token,idDate):

        url = 'http://121.41.14.39:9097/api/message'
        HttpRequests().headers['X-AUTH-TOKEN'] = token

        resp = requests.post(url,json=idDate, headers=HttpRequests().headers)
        return resp



