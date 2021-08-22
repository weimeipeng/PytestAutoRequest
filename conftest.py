'''
Code description:配置信息
Create time: 2021/2/14
Developer: 韦鹏
'''
import os
import pytest
from api.get_token import Get_Token
from common.http_requests import HttpRequests


@pytest.fixture(scope="session")
def get_token():
    '''前置操作获取token并传入headers'''
    Get_Token().get_token()
    if not HttpRequests().params.get("access_token", ""):#没有get到token，跳出用例
        pytest.skip("未获取token跳过用例")
    yield HttpRequests().req
    HttpRequests().req.close()

def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost", action="store", default="http://192.168.1.54:32099",
        help="my option: type1 or type2"
    )
@pytest.fixture(scope="session",autouse=True)
def host(request):
    '''获取命令行参数'''
    #获取命令行参数给到环境变量
    #pytest --cmdhost 运行指定环境
    os.environ["host"] = request.config.getoption("--cmdhost")
    print("当前用例运行测试环境:%s" % os.environ["host"])
