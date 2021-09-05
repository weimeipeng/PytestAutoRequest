from api.api_login import Login
import sys
import allure
import pytest
from common.logger import Log
from common.read_yaml import ReadYaml

testdata = ReadYaml("testLoginData.yaml").get_yaml_data()  # 读取数据

@pytest.mark.skipif(con='全部测试')
@allure.feature('教师系统接口')
class Test_Login(object):
    log = Log()
    @pytest.mark.process
    @pytest.mark.parametrize('data',testdata)
    def test_service_info(self,data):

        username=data['data']['username']

        password=data['data']['password']
        print("测试账号为：" ,username,password)
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,data['detail'])))
        with allure.step(data['detail']):
            msg = Login().login({"username":username,"password":password},mode=False)
        self.log.info('%s:%s' %((sys._getframe().f_code.co_name,'请求结果：%s' % msg.json())))

        #断言
        # assert msg.json()['detail'] == data['detail']
        # assert msg.json()['data']['username'] == data['data']['username']
        # assert msg.json()['data']['password'] == data['data']['password']
        assert msg.json()['code'] == data['resp']['code']
        assert msg.json()['message'] == data['resp']['message']






