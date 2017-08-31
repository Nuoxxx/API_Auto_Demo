import unittest
from API_Auto_Demo.Conf import config
from API_Auto_Demo.Interface import Common

class Home(unittest.TestCase):
    u"""首页接口测试"""
    # sessionKey = ''
    #类方法
    @classmethod
    def setUpClass(cls):
        c = config.Config().get_conf()
        cls.user_info = Common.get_userinfo()
        cls.sessionKey = cls.user_info['item']['sessionKey']
        cls.solution = ''

    @classmethod
    def tearDownClass(cls):
        print("Home test teardown")

    def test_common_product(self):
        u"""获取商品"""
        product_url = Common.get_url('/api/product/GetCommonProductList')
        #获取用户session、地址信息
        areaId = self.user_info['item']['loginUser']['domainCode']
        product_datamap = {'lable':'1','areaId':areaId,'sortId':'3',
                           'pageNumber':'1','pageSize':'20','sessionKey':self.sessionKey}
        product_result = Common.post_request(product_url,product_datamap)
        self.assertEqual('20',product_result['splitPage']['currentPageCount'],u'返回的数据条数不一致')

    def test_solutionlist(self):
        u"""获取行业信息"""
        solution_url = Common.get_url('/api/market/getSolutionsList')
        solution_datamap = {'pageNumber':'1','pageSize':'20','sessionKey':self.sessionKey}
        solution_result = Common.post_request(solution_url,solution_datamap)
        solution_list = solution_result['item']
        # 获取文件路径
        solutionFilePath = solution_list[0]['solutionFilePath']
        solutionFile_url = Common.get_url(solutionFilePath)
        solutionFile_result = Common.get_request(solutionFile_url)
        # print(solutionFile_result)
        self.assertTrue(solutionFile_result)

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Home('test_common_product'))
    # suite.addTest(Home('test_solutionlist'))
    # unittest.TextTestRunner(verbosity=2).run(suite)