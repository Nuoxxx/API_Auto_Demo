import unittest
from API_Auto_Demo.Conf import config
from API_Auto_Demo.Interface import Common

class Home(unittest.TestCase):
    u"""首页接口测试"""

    #类方法
    @classmethod
    def setUpClass(cls):
        c = config.Config().get_conf()

    @classmethod
    def tearDownClass(cls):
        print("Home test teardown")

    def test_common_product(self):
        u"""获取商品"""
        url = Common.get_url('api/product/GetCommonProductList')
        self.assertEqual(True, True)

    def test_solutionlist(self):
        u"""获取行业信息"""
        url = Common.get_url('api/market/getSolutionsList')
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
