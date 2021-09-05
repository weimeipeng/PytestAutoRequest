'''
Code description:头条新闻 服务相关接口
Create time: 2021/2/14
Developer: 韦鹏
'''
import os

import requests

from common.http_requests import HttpRequests


class Api_News_Service(object):

    def __init__(self):
        self.headers = HttpRequests().headers

    def get_hotnews(self):
        url = "http://v.juhe.cn/toutiao/index"
        param_data={'page':3,'key':'e4e13b9352c189d2289d26a97c8ef23c'}
        response = HttpRequests().get(url,headers=self.headers,params=param_data)
        # hot = response.json()['result']['data'][0]['title']
        return response

    def get_weather(self,city):
        url='http://apis.juhe.cn/simpleWeather/query'
        param_data = {'city':city,'key': 'fea71ec5629c802f1c7d64ba57bae351'}
        response = HttpRequests().get(url,params=param_data,headers=self.headers)
        return response

    def get_phone(self,phone,type):
        url="http://apis.juhe.cn/mobile/get"
        param_data = {'phone': phone,'dtype':type ,'key': '6e9a421a23a510891542fcd6a2c167d7'}
        response = HttpRequests().get(url, params=param_data, headers=self.headers)
        return response

    def get_constellation(self,consName):
        url = "http://web.juhe.cn:8080/constellation/getAll"
        param_data = {'consName': consName, 'type': "today", 'key': 'f7aec031a4fcbccdafa7906300d365f8'}
        response = HttpRequests().get(url, params=param_data, headers=self.headers)
        return response


if __name__ == '__main__':
    # print(Api_News_Service().get_weather('杭州').json())
    # print(Api_News_Service().get_phone(13291870920).json())
    print(Api_News_Service().get_constellation('天秤座').json())


