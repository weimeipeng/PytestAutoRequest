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
# from api.api_auth_service.api_auth_service import Api_Auth_Service
from api.api_service import Api_Auth_Service

testdata = ReadYaml("auth_service.yml").get_yaml_data()  # 读取数据


@allure.feature('服务详情')
class Test_Service_Info(object):
    log = Log()

    @pytest.mark.process
    @pytest.mark.parametrize('serviceId,developerId,expect', testdata['service_info'],
                             ids=['服务详情'])
    def test_service_info(self,serviceId,developerId,expect):
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,'------服务详情接口-----')))
        with allure.step('获取服务id'):
            serviceId = Api_Auth_Service().get_service_id()
        with allure.step('服务详情'):
            msg = Api_Auth_Service().api_service_info(serviceId,developerId)
        self.log.info('%s:%s' % ((sys._getframe().f_code.co_name, '获取请求结果：%s' % msg.json())))
        # 断言
        assert msg.json()["result_message"] == expect['result_message']
        assert msg.json()['result_code'] == expect['result_code']
        assert 'url' in msg.json()['data']