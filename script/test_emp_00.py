# 按照设计顺序编写员工模块的增删改查场景测试用例脚本
# 如果能够按照设计顺序实现员工的增删改查，那么就证明，能够对员工模块进行操作了
# 也就证明大家能够使用代码完成接口测试了。

# 导包
import unittest
import logging
import requests
import app
from api.login_api import LoginApi


# 创建测试类
from utils import assert_common_utils


class TestEmp(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()
        # 定义员工模块的URL
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    def tearDown(self):
        pass

    # 编写测试员工增删改查的案例
    def test01_test_emp_operation(self):
        # 1 实现登录接口
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        headers=app.HEADERS)
        #   获取登录接口返回的json数据
        result = response.json()
        # 输出登录的结果
        logging.info("员工模块登录接口的结果为：{}".format(result))
        #   把令牌提取出来，并保存到请求头当中
        token = result.get("data")
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("登录成功后设置的请求头为：{}".format(headers))
        # 断言
        assert_common_utils(self,response,200,True,10000,"操作成功")
        # 2 实现添加员工接口
        response = requests.post(self.emp_url, json={
                                                "username": "尼古6拉斯特斯拉",
                                                "mobile": "18887342567",
                                                "timeOfEntry": "2020-03-16",
                                                "formOfEmployment": 2,
                                                "departmentName": "snowsnow",
                                                "departmentId": "1226092852421177344", "correctionTime": "2020-03-15T16:00:00.000Z"
                                            },
                                 headers=headers)
        # 打印添加的结果
        logging.info("添加员工的结果为：{}".format(response.json()))
        #   获取添加员工返回的json数据
        add_result = response.json()
        #   把员工id提取出来，并保存到变量当中
        emp_id = add_result.get("data").get("id")
        # 打印获取的员工ID
        logging.info("获取员工ID为：{}".format(emp_id))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
        # 3 实现查询员工接口
        # 查询员工的url
        query_emp_url = self.emp_url + "/" + emp_id
        # 打印拼接的URL
        logging.info("查询员工接口的URL为：{}".format(query_emp_url))
        # 发送查询员工的接口请求
        response = requests.get(url=query_emp_url,headers=headers)
        # 打印查询员工的结果
        logging.info("查询员工的结果为：{}".format(response.json()))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

        # 4 实现修改员工接口
        # 修改员工的url
        modify_emp_url = self.emp_url + "/" + emp_id
        # 打印拼接的URL
        logging.info("修改员工接口的URL为：{}".format(modify_emp_url))
        # 发送修改员工的接口请求
        response = requests.put(url=query_emp_url,json={"username": "赵四"},
                                 headers=headers)
        # 打印修改员工的结果
        logging.info("修改员工的结果为: {}".format(response.json()))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")

        # 5 实现删除员工接口
        # 删除员工的url
        delete_emp_url = self.emp_url + "/" + emp_id
        # 打印拼接的URL
        logging.info("删除员工接口的URL为：{}".format(delete_emp_url))
        # 发送删除员工的接口请求
        response = requests.delete(url=query_emp_url,headers=headers)
        # 打印修改员工的结果
        logging.info("删除员工的结果为: {}".format(response.json()))
        # 断言
        assert_common_utils(self, response, 200, True, 10000, "操作成功")
