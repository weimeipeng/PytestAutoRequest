from api.api_login import Login
from common.my_requests import Myrequest
import sys
import allure
import pytest
from common.logger import Log
from common.read_yaml import ReadYaml
import hashlib
import os

def get_md5(psw):
    """
    :param psw: 明文
    :return: 返回加密后密文
    """
    md5 = hashlib.md5()
    md5.update(psw.encode("utf-8"))
    return md5.hexdigest()

testdata = ReadYaml("testLoginData.yaml").get_yaml_data()  # 读取数据

@pytest.mark.skipif()
@allure.feature('教师系统登录2')
class Test_Login(object):
    log = Log()
    @pytest.mark.process
    @pytest.mark.parametrize('data',testdata)
    def test_service_info(self,data):

        username=data['data']['username']

        password=get_md5(data['data']['password'])

        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,data['detail'])))
        with allure.step(data['detail']):
            msg = Login().login({"username":username,"password":password},mode=False).json()
        self.log.info('%s:%s' %((sys._getframe().f_code.co_name,'请求结果：%s' % msg)))

        #断言
        # assert msg.json()['detail'] == data['detail']
        # assert msg.json()['data']['username'] == data['data']['username']
        # assert msg.json()['data']['password'] == data['data']['password']
        # assert msg.json()['code'] == data['resp']['code']
        # assert msg.json()['message'] == data['resp']['message']

        for key, value in dict(data).items():
            print("key", key)
            if key !='detail':
                assert key in dict(msg).keys(), '关键字"{}"不存在源码中!'.format(key)
                # assert value in dict(msg).values(),'关键字"{}"不存在源码中!'.format(value)







