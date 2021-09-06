from api.api_login import Login
import sys
import allure
import pytest

from api.api_messages import Message
from api.get_token import Get_Token
from common.http_requests import HttpRequests
from common.logger import Log
from common.read_yaml import ReadYaml

testdata = ReadYaml("MessageData.yaml").get_yaml_data()  # 读取数据

# @pytest.mark.skipif(con='全部测试')
@allure.feature('教师系统接口：留言信息接口')
class Test_Message(object):
    log = Log()
    @pytest.mark.process
    @pytest.mark.parametrize('data',testdata)
    def test_message(self,data):

        falg=data['data']['token']


        if falg==False:
            token = 'error'
        elif falg == 'null':
            token = ''
        else:
            token = Get_Token().get_token()   #获取有效token


        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,data['detail'])))
        with allure.step(data['detail']):
            msg = Message().message(token)
        self.log.info('%s:%s' %((sys._getframe().f_code.co_name,'请求结果：%s' % msg.json())))

        assert msg.json()['code'] == data['resp']['code']

        assert msg.json()['message'] == data['resp']['message']






