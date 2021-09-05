# @Time : 2021/9/4 21:14 
# @Author : 韦鹏
# @File : demo3.py 
# @Software: PyCharm
import pytest

@pytest.fixture(scope='class')
def login():
    print("开始测试")

class TestLogin:

    def test_01(self):
        print("用例1")

    def test_02(self,login):
        print("用例2")

    def test_03(self):
        print("用例3")

if __name__ == '__main__':
    pytest.main()