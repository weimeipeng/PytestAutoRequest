'''
Code description:头条新闻 服务相关接口
Create time: 2021/2/14
Developer: 韦鹏
'''
import os
from common.http_requests import HttpRequests


class Api_Auth_Service(object):

    def __init__(self):
        self.headers = HttpRequests().headers

    def get_first_hot(self):
        url = "http://v.juhe.cn/toutiao/index"
        param_data={'page':3,'key':'e4e13b9352c189d2289d26a97c8ef23c'}
        response = HttpRequests().get(url,headers=self.headers,params=param_data)
        hot = response.json()['result']['data'][0]['title']
        return hot



if __name__ == '__main__':
    #Auth_Service().api_home_service_list()
    print(Api_Auth_Service().get_first_hot())
    #Auth_Service().api_service_info()