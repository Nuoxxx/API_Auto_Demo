#!/usr/bin/env Python
# coding=utf8
#导入configparser库，用于读取配置文件
import configparser
import os
import sys
sys.path.append('\Conf')
class Config():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(__file__),'conf.ini')
        # print(self.conf_path)
        a = self.config.read(self.conf_path,encoding='utf-8-sig')
        # print(a)
        self.conf = {'host': '', 'user': '', 'password': '',
                     'userName': '', 'passWord': '',
                     'base_url':'', 'success': ''}
        # print("sections:",self.config.sections())

    def get_conf(self):
        """
        配置文件读取，并赋值给全局参数
        :return: 
        """
        self.conf['host'] = self.config.get("test_db",'host')
        self.conf['user'] = self.config.get("test_db", "user")
        self.conf['password'] = self.config.get("test_db", "password")

        self.conf['base_url'] = self.config.get("url","base_url")
        self.conf['userName'] = self.config.get("user_info", "userName")
        self.conf['passWord'] = self.config.get("user_info", "passWord")
        self.conf['success'] = self.config.get("code","success")

        return self.conf

if __name__ == '__main__':
    Config()
