from api.api_exams import Exams
import sys
import allure
import pytest

from api.api_messages import Message
from api.get_token import Get_Token
from common.http_requests import HttpRequests
from common.logger import Log
from common.read_yaml import ReadYaml

testdata = ReadYaml("examsData.yaml").get_yaml_data()  # 读取数据

# @pytest.mark.skipif(con='全部测试')
@allure.feature('教师系统我的练习')
class Test_Exams(object):
    log = Log()
    @pytest.mark.process
    @pytest.mark.parametrize('data',testdata,ids=['{}'.format(i+1) for i in range(len(testdata))] )
    def test_exams(self,data):

        falg=data['data']['token']

        if falg == False:
            token = 'error'
        elif falg == 'null':
            token = ''
        else:
            token = Get_Token().get_token()   #获取有效token


        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,data['detail'])))
        with allure.step(data['detail']):
            msg = Exams().exams(token)
        self.log.info('%s:%s' %((sys._getframe().f_code.co_name,'请求结果：%s' % msg.json())))

        assert msg.json()['code'] == data['resp']['code']

        try:
            message = msg.json()['message']
        except KeyError as e:
            print('接口返回数据中没有:',e)
            message = msg.json()['msg']
            assert message == data['resp']['msg']




