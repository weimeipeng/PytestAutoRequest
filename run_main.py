import os
import pytest

if __name__ == '__main__':
    pytest.main(['-m', 'process', '-s', '--alluredir', 'report/tmp'])  # -m运行mark标记文件
    # os.system('allure generate report/tmp -o report/html --clean')  # /report/tmp 为存放报告的源文件目录
