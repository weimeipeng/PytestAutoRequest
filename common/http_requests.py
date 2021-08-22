'''
Code description: 封装自己的请求类型
Create time: 2021/2/14
Developer: 韦鹏
'''

import requests


# 定义一个HttpRequests的类
class HttpRequests(object):

    req = requests.session()#定义session会话
    # 定义公共请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'cookie':''
    }
    params = {
        'access_token':''
    }
    # 封装自己的get请求,获取资源
    def get(self, url='', params='', data='', headers=None, cookies=None,stream=None,verify=None):
        response = self.req.get(url,params=params,data=data,headers=headers,cookies=cookies,stream=stream,verify=verify)
        return response

    # 封装自己的post方法，创建资源
    def post(self, url='', params='',data='', json='', headers=None, cookies=None,stream=None,verify=None):
        response = self.req.post(url,params=params,data=data,json=json,headers=headers,cookies=cookies,stream=stream,verify=verify)
        return response

    # 封装自己的put方法，更新资源
    def put(self, url='', params='', data='', headers=None, cookies=None,verify=None):
        response = self.req.put(url, params=params, data=data, headers=headers, cookies=cookies,verify=verify)
        return response

    # 封装自己的delete方法，删除资源
    def delete(self, url='', params='', data='', headers=None, cookies=None,verify=None):
        response = self.req.delete(url, params=params, data=data, headers=headers, cookies=cookies,verify=verify)
        return response