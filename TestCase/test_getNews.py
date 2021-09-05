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

@pytest.mark.skipif(con='全部测试')
@allure.feature('聚合接口')
class Test_Service_Info(object):
    log = Log()
    @pytest.mark.process
    def test_News_info(self):
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,'------开始热门新闻查询接口接口测试-----')))
        with allure.step('获取热门新闻'):
            serviceId = Api_News_Service().get_hotnews()
