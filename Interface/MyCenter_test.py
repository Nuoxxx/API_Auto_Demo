#!/usr/bin/env Python
# coding=utf8
import requests
import json
import unittest
import xlrd
import re,sys
from ddt import ddt,data,unpack
#导入配置文件
sys.path.append('\API_Auto_Demo')
from API_Auto_Demo.Conf import config
#导入公共文件Common_test.py
from API_Auto_Demo.Interface import Common

@ddt
class MyCenter(unittest.TestCase):
    '''个人中心接口测试'''

    def setUp(self):
        '''初始化数据'''

        '''获取请求地址'''
        c = config.Config().get_conf()   #调用config.py文件的get_conf()函数

        # '''获取状态码'''
        # self.success = c["success"]      #成功的状态码
        # self.TrackNoIsExist = c["TrackNoIsExist"]      #其它状态码


    def tearDown(self):
        print("tearDown")

    @data((18565687531,123456,''),
          (123,123456,'营销帐号不存在！'),
          (18565687531,000000,'密码认证失败!'))
    @unpack
    def test_user_login(self,d_mobile,pwd,msg):
        u"""登录测试"""
        c = config.Config().get_conf()  # 调用config.py文件的get_conf()函数
        #拼接URL
        url = Common.Get_url("api/user/login")
        print("userinfo url:",url)

        datalist = {"userName": d_mobile, "passWord": pwd}
        headers = {"User-Agent": "okhttp/3.1.2",
                   "Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url, data=datalist, headers=headers)
        #json.loads() 解码：把Json格式字符串解码转换成Python对象
        #json.dumps() 编码：把一个Python对象编码转换成Json字符串
        print("r.text",r.text)
        result = json.loads(r.text)
        print(result)
        r_code = result['code']
        print("返回的code:",r_code)

        if r_code =='0':
            #账号正常登录，需要校验返回的数据和数据库数据是否一致

            #查询数据库数据
            # sql = """select * from pt_seller where (mobile = '18565687531')"""
            sql = """select * from pt_user WHERE mobile = '%s' %(d_mobile)"""
            pt_user_result = Common.Get_Database_data(sql)
            pt_user_data = pt_user_result[0]
            # 性别
            pt_seller_sex = pt_user_data[3]
            # 手机号码
            pt_seller_mobile = pt_user_data[4]
            # 身份认证状态 0：未认证；1：认证通过 ；2：认证中
            pt_seller_identitystatus = pt_user_data[50]

            #服务器返回数据
            r_item = result['item']
            loginUser = r_item['loginUser']

            ser_mobile = loginUser['mobile']
            ser_sex = loginUser['sex']
            ser_identitystatus = loginUser['identityStatus']

            self.assertEqual(pt_seller_sex,ser_sex,u'性别不一致')
            self.assertEqual(pt_seller_mobile,ser_mobile,u'手机号不一致')
            self.assertEqual(pt_seller_identitystatus,ser_identitystatus,u'身份认证不一致')
            print('*****和数据数据一致**********')
        else:
            r_msg = result['msg']
            print(r_msg)
            self.assertEqual(r_msg,msg)


    def test_database(self):
        u"""获取Session Key"""
        session_Key = Common.Get_Cookie()
        print("MyCenter:",session_Key)
        # 每一组数据是以元组的形式返回的[(),()]
        # sql = """select * from pt_seller where (mobile LIKE  '1856568753%')"""
        # c_result = Common.Get_Database_data(sql)

        self.assertTrue(True)