# @Time : 2021/9/4 21:39 
# @Author : 韦鹏
# @File : demo4_params.py 
# @Software: PyCharm
import pytest

# @pytest.fixture(params=[1,2,{'a':1,'b':2},(4,5,6)])
# def demo(request):
#     return request.param
#
# def test_f(demo):
#     print('{}'.format(demo))

@pytest.mark.parametrize('arg',['abc',1,{'a':1,'b':2},(1,3,4)])
def test_01(arg):
    print('传入的值为：{}'.format(arg))
    # assert arg == 1
    assert isinstance(arg,dict) or isinstance(arg,tuple)

if __name__ == '__main__':
    pytest.main()