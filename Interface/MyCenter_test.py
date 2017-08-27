# -*- coding: utf-8 -*-
import requests
import json
import unittest
import xlrd
import re
from ddt import ddt,data,unpack
#导入配置文件
from API_Auto.Conf import config
#导入公共文件Common_test.py
from API_Auto.Interface import Common

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
    def test_user_login(self,mobile,pwd,msg):
        u"""登录测试"""
        c = config.Config().get_conf()  # 调用config.py文件的get_conf()函数
        #拼接URL
        url = Common.Get_url("api/user/login")
        print("userinfo url:",url)

        datalist = {"userName": mobile, "passWord": pwd}
        headers = {"User-Agent": "okhttp/3.1.2",
                   "Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url, data=datalist, headers=headers)

        result = json.loads(r.text)
        print(result)
        r_code = result['code']
        print("返回的code:",r_code)
        if r_code =='0':
            self.assertTrue(True)
        else:
            r_msg = result['msg']
            print(r_msg)
            self.assertEqual(r_msg,msg)

    def test_addtrackno_success(self):
        u"""获取Session Key"""
        session_Key = Common.Get_Cookie()
        print("MyCenter:",session_Key)
        self.assertTrue(True)