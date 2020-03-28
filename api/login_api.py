# ihrm人力资源管理系统伪代码
# response = requests.post("http://182.92.81.159/api/sys/login", json={"mobile":"","password":""})

import requests


# 定义封装的登录API类
class LoginApi:
    def __init__(self):
        # 定义IHRM登录的url
        self.login_url = "http://182.92.81.159/api/sys/login"

    # 定义封装的登录函数
    def login(self,jsonData,headers):
        response = requests.post(self.login_url,json=jsonData,headers=headers)
        return response

# 防止导入模块时执行写在类外面的代码
if __name__ == '__main__':
    login_api = LoginApi()
    jsonData = {"mobile":"13800000002","password":"123456"}
    headers = {"Content-Type":"application/json"}
    response = login_api.login(jsonData, headers)
    print("登录结果为：", response.json())
