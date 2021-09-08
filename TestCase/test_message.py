from api.api_login import Login
import sys
import allure
import pytest

from api.api_messages import Message
from api.get_token import Get_Token
from common.logger import Log
from common.read_yaml import ReadYaml

testdata = ReadYaml("MessageData.yaml").get_yaml_data()  # 读取数据

# @pytest.mark.skipif(con='全部测试')
@allure.feature('教师系统获取留言')
class Test_Message(object):
    log = Log()
    @pytest.mark.process
    @pytest.mark.parametrize('data',testdata['get_message'])
    def test_get_message(self,data):
        falg=data['data']['token']
        if falg==False:
            token = 'error'
        elif falg == 'null':
            token = ''
        else:
            token = Get_Token().get_token()   #获取有效token
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,data['detail'])))
        with allure.step(data['detail']):
            msg = Message().get_message(token)
        self.log.info('%s:%s' %((sys._getframe().f_code.co_name,'请求结果：%s' % msg.json())))

        assert msg.json()['code'] == data['resp']['code']

        # assert msg.json()['message'] == data['resp']['message']
        try:
            message = msg.json()['message']
        except KeyError as e:
            print('接口返回数据中没有:',e)
            message = msg.json()['msg']
        finally:
            assert message == data['resp']['msg']


    @pytest.mark.process
    @pytest.mark.parametrize('data',testdata['push_message'])
    def test_push_message(self,data):

        inData={"title":data['data']['title'],"content":data['data']['content'],"time":data['data']['time']}
        falg=data['data']['token']
        if falg == False:
            token = 'error'
        elif falg == 'null':
            token = ''
        else:
            token = Get_Token().get_token()   #获取有效token
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,data['detail'])))
        with allure.step(data['detail']):
            msg = Message().push_message(token,inData)
        self.log.info('%s:%s' %((sys._getframe().f_code.co_name,'请求结果：%s' % msg.json())))
        assert msg.json()['code'] == data['resp']['code']
        # assert msg.json()['message'] == data['resp']['message']
        try:
            message = msg.json()['message']
        except KeyError as e:
            print('接口返回数据中没有:',e)
            message = msg.json()['msg']
        finally:
            assert message == data['resp']['msg']






