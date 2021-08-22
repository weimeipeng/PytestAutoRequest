'''
Code description: 配置连接数据库
Create time: 2021/2/14
Developer: 韦鹏
'''
import pymysql

dbinfo = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"root",
    "port":3306
}
class DbConnect():
    def __init__(self,db_conf,database=""):
        self.db_conf = db_conf
        #打开数据库
        self.db = pymysql.connect(database = database,
                                  cursorclass = pymysql.cursors.DictCursor,
                                  **db_conf)
        #使用cursor()方式获取操作游标
        self.cursor = self.db.cursor()

    def select(self,sql):
        #sql查询
        self.cursor.execute(sql)#执行sql
        results = self.cursor.fetchall()
        return results

    def execute(self,sql):
        #sql 删除 提示 修改
        try:
            self.cursor.execute(sql)#执行sql
            self.db.commit()#提交修改
        except:
            #发生错误时回滚
            self.db.rollback()

    def close(self):
        self.db.close()#关闭连接

def select_sql(select_sql):
    '''查询数据库'''
    db = DbConnect(dbinfo,database='test')
    result = db.select(select_sql)
    db.close()
    return result

def execute_sql(sql):
    '''执行SQL'''
    db = DbConnect(dbinfo,database='test')
    db.execute(sql)
    db.close()

if __name__ == '__main__':
    sql = "SELECT * FROM test.employee where employee_id=1"
    sel = select_sql(sql)[0]['employee_name']
    print(sel)