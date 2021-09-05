# @Time : 2021/9/4 20:56 
# @Author : 韦鹏
# @File : demo1.py 
# @Software: PyCharm

import pytest

@pytest.fixture()
def login():
    print("打开浏览器")
    a="登录"
    return a

@pytest.fixture()
def logout():
    print("关闭浏览器")

class TestLogin:
    def test_01(self,login):
        print('001传入loging fixture')
        assert login=="登录"

    def test_02(self,logout):
        print('002传入logout fixture')

    def test_03(self,login,logout):
        print('003传入login \ logout fixture')

    def test_04(self):
        print('004 没有传入任何')

if __name__ == '__main__':
    pytest.main()
