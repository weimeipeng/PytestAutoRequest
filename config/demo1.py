# @Time : 2021/9/5 21:58 
# @Author : 韦鹏
# @File : demo1.py 
# @Software: PyCharm

import pytest
userinfo = [('张三',123),('李四','pwd')]

@pytest.fixture()
def login_user(request):
    user = request.param
    print('传入的用户名：{}'.format(user))
    return user

@pytest.fixture()
def login_pwd(request):
    pwd = request.param
    print("密码为：{}".format(pwd))
    return pwd

@pytest.mark.parametrize('login_user,login_pwd',userinfo,indirect=True)
def test_01(login_user,login_pwd):
    print("测试类的读到用户是{},密码是{}".format(login_user,login_pwd))

if __name__ == '__main__':
    pytest.main()