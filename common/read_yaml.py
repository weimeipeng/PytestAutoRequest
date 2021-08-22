'''
Code description: 读取yml文件测试数据
Create time: 2021/2/14
Developer: 韦鹏
'''
import os
import yaml
import getpathinfo
class ReadYaml():
    def __init__(self,filename):
        path = getpathinfo.get_path()#获取本地路径
        self.filepath = os.path.join(path,'data','test_data')+"/"+filename#拼接定位到data文件夹

    def get_yaml_data(self):
        with open(self.filepath, "r", encoding="utf-8")as f:
            # 调用load方法加载文件流
            return yaml.load(f,Loader=yaml.FullLoader)

if __name__ == '__main__':
    data = ReadYaml("auth_service.yml").get_yaml_data()['add_or_update_service']
    print(data)