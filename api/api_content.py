from common.http_requests import HttpRequests


class Api_Content_Service(object):

    def __init__(self):
        self.headers = HttpRequests().headers

    def get_xiaohua(self,sort=None,time=None):
        url='http://v.juhe.cn/joke/content/list.php'
        key='c9e2444ef7ce61627fad5a2a62427042'
        param_data={'key':key,'sort':sort,'time':time}
        reponse=HttpRequests().get(url,params=param_data,headers=self.headers)
        return  reponse




if __name__ == '__main__':
    print(Api_Content_Service().get_xiaohua('desc').json())