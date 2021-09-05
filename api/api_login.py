
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

    data={'flag': '松勤教育', 'code': 200, 'message': '登录成功', 'data': {'studentId': 20200015, 'studentName': '小王15', 'grade': '2020', 'major': '信息工程', 'clazz': '2', 'institute': '软件工程学院', 'tel': '13500000000', 'email': 'sqqd@163.com', 'pwd': '', 'cardId': '33042419891212158', 'sex': '男', 'role': '2'}, 'token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiLlsI_njosxNSIsInN1YiI6IuWwj-eOizE1IiwiaWF0IjoxNjMwNjQxMjU0fQ.L9FZW31yFgIODKEjWPZnWq7VhOMsWBkm6mq5t3Dffho'}
    msg = Login().login({"username":"20200015","password":"123456"},False).json()
    print(msg)


