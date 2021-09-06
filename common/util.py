# @Time : 2021/9/6 21:54 
# @Author : 韦鹏
# @File : util.py 
# @Software: PyCharm
import hashlib

class Util(object):

    def get_md5(self,psw):
        """
        :param psw: 明文
        :return: 返回加密后密文
        """
        md5 = hashlib.md5()
        md5.update(psw.encode("utf-8"))
        return md5.hexdigest()

