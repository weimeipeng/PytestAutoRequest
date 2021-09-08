'''
Code description: 服务详情
Create time: 2021/2/14
Developer: 韦鹏
'''
import sys
import allure
import pytest
from common.logger import Log
from common.read_yaml import ReadYaml
from api.api_News import Api_News_Service

testdata = ReadYaml("getPhoneData.yaml").get_yaml_data()  # 读取数据

@pytest.mark.skipif()
@allure.feature('手机号查询')
class Test_Info(object):
    log = Log()

    @pytest.mark.process
    @pytest.mark.parametrize('data', testdata)
    def test_phone(self, data):
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name, '------开始手机号码归属地查询接口测试-----')))
        with allure.step('手机号查询接口'):
            msg = Api_News_Service().get_phone(data['data']['phone'],data['data']['type'])
        self.log.info('%s:%s' % ((sys._getframe().f_code.co_name, '获取请求结果：%s' % msg.json())))
        # # 断言
        assert msg.json()["resultcode"] == data['resp']['resultcode']
        #缺少内容断言
        assert msg.json()['error_code'] == data['resp']['error_code']

