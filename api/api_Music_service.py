'''
Code description:网易云音乐 服务相关接口
Create time: 2021/2/14
Developer: 韦鹏
'''
import os
from common.http_requests import HttpRequests


class Api_Auth_Service(object):

    def __init__(self):
        self.headers = HttpRequests().headers

    def get_first_hot(self):
        url = "http://172.31.128.199:3000/search/hot"
        response = HttpRequests().get(url,headers=self.headers)
        hot = response.json()['result']['hots'][0]['first']
        return hot



if __name__ == '__main__':
    #Auth_Service().api_home_service_list()
    print(Api_Auth_Service().get_first_hot())
    #Auth_Service().api_service_info()