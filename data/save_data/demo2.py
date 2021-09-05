# @Time : 2021/9/4 21:05 
# @Author : 韦鹏
# @File : demo2.py.py 
# @Software: PyCharm
import pytest

@pytest.fixture()
def account():
    a='account'
    print('第一层fixture')
    return a

@pytest.fixture()
def login():
    print('第二层fixture')

class TestLogin:
    def test_1(self,login):
        print('直接使用第二层的fixture，返回的值为{}'.format(login))

    def test_2(self,account):
        print('只调用account fixture,返回值为{}'.format(account))

if __name__ == '__main__':
    pytest.main()