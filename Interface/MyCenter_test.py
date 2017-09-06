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
    base_url = ''
    @classmethod
    def setUpClass(cls):
        '''初始化数据'''
        c = config.Config().get_conf()   #调用config.py文件的get_conf()函数
        cls.base_url = c["base_url"]
    @classmethod
    def tearDownClass(cls):
        print("tearDown")

    @data({'userName':18565687531,'passWord':123456,'msg':''},
          {'userName':1231,'passWord':123456,'msg':'营销帐号不存在！'},
          {'userName':18565687531,'passWord':000000,'msg':'密码认证失败!'},
          {'userName':18565687531,'passWord':'','msg': '用户名或密码不能为空！'},
          {'userName':'','passWord':123456,'msg': '用户名或密码不能为空！'},
          {'userName': 18565687531, 'msg': '用户名或密码不能为空！'})
    # unpack 将一个用例的参数分解开，按照（不定）参数传递
    @unpack
    # 支持不定参数  **kwargs 传入不定数量的键值对
    def test_user_login(self,**kwargs):

        u"""登录测试"""
        url = Common.get_url(self.base_url,'/api/user/login')
        # 发送post请求，将返回的JSon数据放在result中
        result = Common.post_request(url,kwargs)
        r_code = result['code']

        d_mobile = kwargs['userName']
        msg = kwargs['msg']

        if r_code =='0':
            #账号正常登录，需要校验返回的数据和数据库数据是否一致

            #查询数据库数据
            # 每一组数据是以元组的形式返回的[(),()]
            # sql = """select * from pt_seller where (mobile LIKE  '1856568753%')"""
            # c_result = Common.get_database_data(sql)

            # 将数据格式化输出
            # sql = "select * from pt_seller where mobile = "+('%s' %(d_mobile))
            # mobile本身为int类型，转成string类型
            sql = "select * from pt_seller where mobile = " + str(d_mobile)
            # 数据库查询结果
            pt_user_result = Common.get_database_data(sql)
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
            print('*****服务器返回和数据库数据一致**********')
        else:
            #未登录成功，校验服务器返回的报错信息和文档中内容是否一致
            r_msg = result['msg']
            self.assertEqual(r_msg,msg,u'和预期结果不一致')


    def test_Sessionkey(self):
        u"""获取Session Key"""
        session_Key = Common.get_cookie()
        print("MyCenter:",session_Key)

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()