# @Time : 2021/9/6 22:18 
# @Author : 韦鹏
# @File : api_score.py
# @Software: PyCharm
# @Function  我的分数


import requests
#加载测试数据
from common.http_requests import HttpRequests
from common.read_yaml import ReadYaml
from api.get_token import Get_Token


class Score(object):
    def score(self,token):

        url='http://121.41.14.39:9097/api/score/1/10/20200015'

        HttpRequests().headers['X-AUTH-TOKEN']=token

        resp = requests.get(url,headers=HttpRequests().headers)
        return resp



