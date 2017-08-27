import time, os
import sys
sys.path.append('./Interface')

from API_Auto.API_Auto_Demo.Conf import config#导入配置文件
import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './Interface'

file = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    config.Config().get_conf()      #初始化配置文件
    #测试结果显示在控制台
    # runner = unittest.TextTestRunner()
    # runner.run(file)

    # 测试结果生成HTML文件
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    public_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    # 不同系统的路径分隔符不一样，os.sep --返回路径各部分之间的分隔符，linux是'/'，
    # windows是'\\'，由于'\'在python中会转义，所以返回值是两个'\'   ==　os.path.sep
    filename = public_path + os.sep+"Report"+os.sep + now + "report.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="接口自动化报告",
                            description="详细描述如下："
                            )
    runner.run(file)
    fp.close()