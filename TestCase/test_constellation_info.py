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

testdata = ReadYaml("ConstellationData.yaml").get_yaml_data()  # 读取数据

@allure.feature('聚合接口')
class Test_Service_Info(object):
    log = Log()

    @pytest.mark.process
    @pytest.mark.parametrize('data',testdata)
    def test_constellation_info(self, data):
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name, '------开始星座运势查询接口测试-----')))
        with allure.step('星座运势查询接口'):
            msg = Api_News_Service().get_constellation(data['data']['consName'])
        self.log.info('%s:%s' % ((sys._getframe().f_code.co_name, '获取请求结果：%s' % msg.json())))
        # # 断言
        assert data['resp']['result'] in (str)(msg.json()), '关键字"{}"不存在源码中!'.format(msg.json())
        assert msg.json()['resultcode'] == data['resp']['resultcode']
        assert msg.json()['error_code'] == data['resp']['error_code']
