#!/usr/bin/env Python
# coding=utf-8
import sys
sys.path.append('\Conf')
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

def get_database_data(state,*Msql):
    '''初始化数据'''
    c = config.Config().get_conf()   #调用config.py文件的get_conf()函数

    '''数据库配置'''
    db_host = c["host"]
    db_user = c["user"]
    db_password = c["password"]

    '''连接Oracle数据库'''
    tns = cx_Oracle.makedsn(db_host,1521,'orcl')
    db = cx_Oracle.connect(db_user, db_password,tns)

    cr = db.cursor()
    # SQL查询语句  # cr.execute("select * from dual")
    cr.execute(state,*Msql)

    result = cr.fetchall()

    '''关闭数据库连接'''
    cr.close()
    db.close()
    # 返回的结果是个list，里面放置的tuple类型的数据
    return result      #返回查询结果

def get_cookie():
    result = get_userinfo()
    sessionKey = result['item']['sessionKey']
    return sessionKey

def get_userinfo():
    c = config.Config().get_conf()  # 调用config.py文件的get_conf()函数
    url = get_url(c["base_url"],'/api/user/login')
    username = c["userName"]
    userpwd = c["passWord"]
    cookie_datamap = {"userName": username, "passWord": userpwd}
    result = post_request(url, cookie_datamap)
    return result

def get_request(url):
    r = requests.get(url,verify = False)
    if (r.status_code == 200 or r.status_code == 304):
        return True
    else:
        return False

# post方法，返回JSon格式数据
def post_request(url,datamap):

    headers = {"User-Agent": "okhttp/3.1.2",
               "Content-Type": "application/x-www-form-urlencoded"}
    # verify = False如果不设置的话，用https格式的请求会报SSL错误,设置为False可以忽略验证SSL证书；
    r = requests.post(url, data=datamap, headers=headers,verify = False)
    # json.loads() 解码：把Json格式字符串解码转换成Python对象
    # json.dumps() 编码：把一个Python对象编码转换成Json字符串
    # 服务器返回的状态码200说明接口正常响应，否则需要异常处理
    if r.status_code == 200:
        return json.loads(r.text)
    else:
        r.raise_for_status()
        return None

# 获取完整url地址
def get_url(baseurl,url):
    # c = config.Config().get_conf()  # 调用config.py文件的get_conf()函数
    return (baseurl + url)

#解析JSon数据
def get_json(Jdata,key):
    pass
