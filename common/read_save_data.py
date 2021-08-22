'''
Code description: 读取保存数据
Create time: 2021/2/14
Developer: 韦鹏
'''
import os
import yaml
import getpathinfo
class Read_Save_Date():
    def __init__(self):
        path = getpathinfo.get_path()#获取本地路径
        self.head_img_path = os.path.join(path,'data','save_data')+"/"+'head_img_path.txt'# head_img_path文件地址
        self.order_id_path = os.path.join(path, 'data', 'save_data') + "/" + 'order_id.txt'  # order_id.txt文件地址

    def get_head_img_path(self):
        # 获取head_img_path
        with open(self.head_img_path, "r", encoding="utf-8")as f:
            return f.read()

    def get_order_id(self):
        # 获取order_id
        with open(self.order_id_path, "r", encoding="utf-8")as f:
            return f.read()

if __name__ == '__main__':
    print(Read_Save_Date().get_head_img_path())
    print(Read_Save_Date().get_order_id())