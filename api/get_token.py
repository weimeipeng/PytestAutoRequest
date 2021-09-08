'''
Code description：获取token
Create time: 2021/2/14
Developer: 韦鹏
'''
import os
from api.api_login import Login
from common.http_requests import HttpRequests


class Get_Token(object):

    def get_token(self,username='20200015',password='123456'):


        token=Login().login({"username":username,"password":password},True)



        #url = "http://192.168.2.199:9092/v1/auth/developer/accountLogin"
        # url = os.environ["host"]+"/v1/auth/developer/accountLogin"
        # body = {
        #     "account": account,
        #     "password": password,
        # }
        # urllib3.disable_warnings()
        # r = HttpRequests().post(url, json=body,verify=False)
        # #print(r.json())
        # token = r.json()['data']['token']
        params = {
            "access_token": token
        }
        HttpRequests().params.update(params)#更新token到session
        return token

if __name__ == '__main__':
    print(Get_Token().get_token())