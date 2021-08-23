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
from api.api_News import Api_News_Service

testdata = ReadYaml("auth_service.yml").get_yaml_data()  # 读取数据


@allure.feature('服务详情')
class Test_Service_Info(object):
    log = Log()
    @pytest.mark.process
    @pytest.mark.parametrize('expect', testdata['weather'],ids=['服务详情'])
    def test_service_info(self,expect):

        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,'------服务详情接口-----')))
        with allure.step('获取热门新闻'):
            serviceId = Api_News_Service().get_first_hot()
            print(serviceId)
        with allure.step('城市天气详情'):
            msg = Api_News_Service().get_weather('杭州')
        self.log.info('%s:%s' % ((sys._getframe().f_code.co_name, '获取请求结果：%s' % msg)))
        # # 断言
        assert msg.json()["reason"] == expect['reason']
        assert msg.json()['error_code'] == expect['error_code']
        # assert '杭州' in msg.json()['result']