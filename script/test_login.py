import logging
import unittest

import app
from api.login_api import LoginApi
from utils import assert_common_utils


class TestLogin(unittest.TestCase):

    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()
    def tearDown(self):
        pass

    # 编写测试的函数
    # 登录成功
    def test01_login_success(self):
        jsonData = {"mobile":"13800000002","password":"123456"}
        response = self.login_api.login(jsonData,app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000,response.json().get("code"))
        # self.assertIn("操作成功",response.json().get("message"))
        # 导入封装的断言通用函数
        assert_common_utils(self,response,200,True,10000,"操作成功")

    # 密码错误
    def test02_password_is_error(self):
        jsonData = {"mobile": "13800000002", "password": "1234567"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 账号不存在
    def test03_mobile_is_not_exist(self):
        jsonData = {"mobile": "13900000002", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 输入的手机号码有英文字符
    def test04_mobile_has_eng(self):
        jsonData = {"mobile": "1380000000x", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 手机号码有特殊字符
    def test05_mobile_has_special(self):
        jsonData = {"mobile": "1380000000@", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 手机号码为空
    def test06_moible_is_empty(self):
        jsonData = {"mobile":"", "password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 密码为空
    def test07_password_is_empty(self):
        jsonData = {"mobile": "13800000002", "password": ""}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 多参-多出1个参数
    def test08_more_params(self):
        jsonData = {"mobile": "13800000002", "password": "123456","sign":"123"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
    # 少参-缺少mobile
    def test09_less_mobile(self):
        jsonData = {"password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 少参-缺少password
    def test10_less_password(self):
        jsonData = {"mobile": "13800000002"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 无参
    def test11_none_params(self):
        jsonData = None
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")
    # 错误参数--输入错误的参数
    def test12_params_is_error(self):
        jsonData = {"mboile":"13800000002","password": "123456"}
        response = self.login_api.login(jsonData, app.HEADERS)
        logging.info("登录成功的结果为: {}".format(response.json()))
        # 导入封装的断言通用函数
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

