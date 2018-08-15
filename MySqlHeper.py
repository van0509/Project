# -*- coding:utf-8 -*-
'''
@project=爬虫
@file=request_proyx
@Author=Administrator
@creat_time=2018/8/1320:34
'''
import pymysql
class DBHelper:
    '''
    完成所有对mysql数据库的处理
    '''

    def __init__(self, host='localhost', port=3306, user='root', pwd='123456', db='seven', charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        self.charset = charset
        self.conn = None  # 连接
        self.cur = None  # 游标

    def connectDataBase(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pwd, db=self.db,
                                        charset=self.charset)
        except:
            print('conn Error')
            return False
        self.cur = self.conn.cursor()
        return True

    def close(self):
        '''
            关闭数据库
        '''

        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

        return True

    def execute(self, sql, params=None):
        if self.connectDataBase() == False:
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
                self.conn.commit()
        except:
            print('execute:' + sql + 'error')
            return False
        return True


# if __name__ == '__main__':
#     dbhelper = DBHelper()
#     # 插入一条数据
#     title = "英雄本色"
#     actor = "周润发"
#     time = "2010-08-17"
#     sql = "INSERT INTO seven.maoyan(title,actor,time) VALUES(%s,%s,%s)"
#     params = (title, actor, time)
#     result = dbhelper.execute(sql, params)
#     if (result == True):
#         print("Insert Ok")
#     else:
#         print("Insert Failed")
#     print(dbhelper.close())
