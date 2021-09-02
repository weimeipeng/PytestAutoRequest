'''
@Code description: 
@File : my_requests.py 
@Time : 2021-09-02 16:17 
@Author : 韦鹏
@Software: PyCharm
'''
from common.http_requests import HttpRequests

class Myrequest:

    def myrequest(self,url,payload):
        url = 'http://121.41.14.39:9097/api/loginS'
        # inData["password"] = get_md5(inData["password"])  # 加密参数中的密码信息
        # payload = inData
        resp = HttpRequests.post(url, json=payload)