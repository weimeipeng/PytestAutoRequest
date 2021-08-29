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

testdata = ReadYaml("auth_service.yml").get_yaml_data()  # 读取数据


@allure.feature('聚合接口')
class Test_Service_Info(object):
    log = Log()

    @pytest.mark.process
    @pytest.mark.parametrize('phone,dtype,expect', testdata['get_phone'],
                             ids=['手机号码归属地查询接口:正确请求','返回类型为空，默认json正确请求','手机号为空，异常校验'])
    def test_phone(self, phone,dtype,expect):
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name, '------开始手机号码归属地查询接口测试-----')))
        with allure.step('手机号查询接口'):
            msg = Api_News_Service().get_phone(phone)
        self.log.info('%s:%s' % ((sys._getframe().f_code.co_name, '获取请求结果：%s' % msg.json())))
        # # 断言
        assert msg.json()["resultcode"] == expect['resultcode']
        #缺少内容断言
        assert msg.json()['error_code'] == expect['error_code']

