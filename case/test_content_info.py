from api.api_content import Api_Content_Service
import sys
import allure
import pytest
from common.logger import Log
from common.read_yaml import ReadYaml

testdata = ReadYaml("auth_service.yml").get_yaml_data()  # 读取数据

@allure.feature('服务详情')
class Test_Service_Info(object):
    log = Log()
    @pytest.mark.process
    @pytest.mark.parametrize('sort,time,expect',testdata['xiaohua'])
    def test_service_info(self,sort,time,expect):

        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,'------开始测试获取笑话大全接口-----')))
        with allure.step('获取笑话大全接口---正常访问'):
            msg = Api_Content_Service().get_xiaohua(sort,time)
        self.log.info('%s:%s' %((sys._getframe().f_code.co_name,'请求结果：%s' % msg.json())))

        #断言
        assert msg.json()['reason'] == expect['reason']
        assert msg.json()['error_code'] == expect['error_code']
        assert expect['result'] in (str)(msg.json()['result'])





