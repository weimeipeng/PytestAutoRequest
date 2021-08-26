
import requests
import hashlib

#加载测试数据
from common.read_yaml import ReadYaml

testdata = ReadYaml('testLoginData.yaml').get_yaml_data()

def get_md5(psw):
    """
    :param psw: 明文
    :return: 返回加密后密文
    """

    md5 = hashlib.md5()
    md5.update(psw.encode("utf-8"))
    return md5.hexdigest()

class Login:
    def login(self,inData,mode=True):

        url='http://121.41.14.39:9097/api/loginS'
        inData["password"] = get_md5(inData["password"]) #加密参数中的密码信息
        payload = inData
        resp = requests.post(url,json=payload)
        if mode:
            return resp.json()['token']
        else:
            return resp

if __name__ == '__main__':
    print(Login().login({"username":"20200015","password":"123456"},False).json())
    # print(testdata.json())
