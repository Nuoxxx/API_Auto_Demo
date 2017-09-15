import unittest
from API_Auto_Demo.Conf import config
from API_Auto_Demo.Interface import Common

class Home(unittest.TestCase):
    u"""首页接口测试"""
    base_url = ''
    #类方法
    @classmethod
    def setUpClass(cls):
        c = config.Config().get_conf()
        cls.base_url = c["base_url"]
        cls.user_info = Common.get_userinfo()
        cls.sessionKey = cls.user_info['item']['sessionKey']
        cls.solution = ''
        # cls.product_result = ''

    @classmethod
    def tearDownClass(cls):
        print("Home test teardown")

    def get_product(self):
        product_url = Common.get_url(self.base_url, '/api/product/GetCommonProductList')
        # 获取用户session、地址信息
        areaId = self.user_info['item']['loginUser']['domainCode']
        product_datamap = {'lable': '1', 'areaId': areaId, 'sortId': '3',
                           'pageNumber': '1', 'pageSize': '20', 'sessionKey': self.sessionKey}
        return Common.post_request(product_url, product_datamap)

    def test_common_product(self):
        u"""获取商品"""
        self.product_result = self.get_product()
        self.assertEqual('20',self.product_result['splitPage']['currentPageCount'],u'返回的数据条数不一致')

    def test_solutionlist(self):
        u"""获取行业信息"""
        solution_url = Common.get_url(self.base_url,'/api/market/getSolutionsList')
        solution_datamap = {'pageNumber':'1','pageSize':'20','sessionKey':self.sessionKey}
        solution_result = Common.post_request(solution_url,solution_datamap)
        solution_list = solution_result['item']
        # 获取文件路径
        solutionFilePath = solution_list[0]['solutionFilePath']
        solutionFile_url = Common.get_url(self.base_url,solutionFilePath)
        solutionFile_result = Common.get_request(solutionFile_url)
        # print(solutionFile_result)
        self.assertTrue(solutionFile_result)

    def test_myProductDetails(self):
        u"""商品详情页"""
        productDetail_url = Common.get_url(self.base_url, '/api/product/myProductDetails')
        product_res = self.get_product()
        print(product_res)
        #选择商品
        product = product_res['item'][0]
        # ids对应pt_product_info表中ids主键
        productDIds = product['ids']
        # pids 对应pt_product表中ids主键
        productIds = product['pids']


        details_datamap = {'User-Agent': '(HUAWEI MT7-TL10,6.0-865164021263221)', 'productDIds': productDIds,
                           'productIds': productIds,'sessionKey': self.sessionKey}
        product_details = Common.post_request(productDetail_url, details_datamap)


        if(product_details['code']=='0'):
            #比较商品名字（sp_name,detailName）、价格

            sql_product = """select p.name from pt_product p  where p.ids = :1"""
            sql_detail =  "select pi.nickname,pi.settle_price from pt_product_info pi where pi.ids = :1 "
            pt_product_result = Common.get_database_data(sql_product,(productIds,))
            pt_productD_result = Common.get_database_data(sql_detail,(productDIds,))

            # self.assertEqual(pt_productD_result[0],product['sp_name'],"nickname Error")
            self.assertEqual(pt_product_result[0][0],product['name'],"name Error")
            self.assertEqual(pt_productD_result[0][1], product['platform_price'], "price Error")

        else:
            print("False")
        # self.assertEqual('20', self.product_result['splitPage']['currentPageCount'], u'返回的数据条数不一致')
        # pass

if __name__ == '__main__':
    unittest.main()
