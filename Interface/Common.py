#!/usr/bin/env Python
# coding=utf-8
import sys
sys.path.append('\API_Auto_Demo')
from API_Auto_Demo.Conf import config #导入Conf文件夹下的config.py文件，用于初始化配置文件
# import pymssql                #导入pymssql，用于连接SqlServer
import requests
import json
import cx_Oracle
import os

# os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.ZHS16GBK'

# def Get_TrackNo():
#     '''初始化数据'''
#     c = Conf.config.Config().get_conf()   #调用config.py文件的get_conf()函数
#
#     '''数据库配置'''
#     db_host = c["host"]
#     db_user = c["user"]
#     db_password = c["password"]
#     db_test_buyer = c["db_test_buyer"]
#     db_test_user = c["db_test_user"]
#
#     '''连接SqlServer数据库'''
#     conn_buyer = pymssql.connect(host=db_host, user=db_user, password=db_password, database=db_test_buyer)
#     cur_buyer = conn_buyer.cursor()
#     sql_buyer =sql = 'SELECT TrackNO FROM TrackInfo02 WHERE (Email = '123@qq.com')'
#     cur_buyer.execute(sql_buyer)
#     trackno_result = cur_buyer.fetchall()
#
#     '''关闭数据库连接'''
#     cur_buyer.close()
#     cur_user.close()
#
#     return trackno_result      #返回单号列表结果

def Get_Database_data(Msql):
    '''初始化数据'''
    c = config.Config().get_conf()   #调用config.py文件的get_conf()函数

    '''数据库配置'''
    db_host = c["host"]
    db_user = c["user"]
    db_password = c["password"]

    '''连接Oracle数据库'''
    tns = cx_Oracle.makedsn(db_host,1521,'orcl')
    db = cx_Oracle.connect(db_user, db_password,tns)
    # charset = 'AMERICAN_AMERICA.ZHS16GBK'),database = 'zcst_yd'
    # db = cx_Oracle.connect('zcst_cs','zcst315315','112.35.4.250:1521/orcl')

    cr = db.cursor()
    # cr.execute("select * from dual")
    # SQL插入语句

    cr.execute(Msql)
    result = cr.fetchall()
    print("SQL查询结果：",result)

    '''关闭数据库连接'''
    cr.close()
    db.close()

    return result      #返回查询结果

def Get_Cookie():
    c = config.Config().get_conf()   #调用config.py文件的get_conf()函数
    url = Get_url('api/user/login')
    print("url:",url)

    username =c["userName"]
    userpwd = c["passWord"]


    datalist = {"userName": username, "passWord": userpwd}
    headers = {"User-Agent": "okhttp/3.1.2",
               "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url, data=datalist, headers=headers)

    result = json.loads(r.text)
    print(result)
    sessionKey = result['item']['sessionKey']
    print(sessionKey)
    return sessionKey

def get_request():
    pass

def post_request():
    pass

def Get_url(url):
    c = config.Config().get_conf()  # 调用config.py文件的get_conf()函数
    return (c["base_url"] + url)

#解析JSon数据
def Get_Json(Jdata,key):

    pass
