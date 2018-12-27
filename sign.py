import requests
from config import SIGN_API, CONFIG
from params_tool import params2str


class Sign(object):
    # 获取新的ios设备信息
    def getDevice(self):
        resp = requests.get(CONFIG['DEVICE_API']).json()
        device_info = resp['data']
        # print("设备信息: " + str(device_info))
        return device_info

    # 获取Token（有效期60分钟）
    def getToken(self):
        resp = requests.get(CONFIG['TOKEN_API']).json()
        token = resp['token']
        # print("Token: " + token)
        return token

    # 使用拼装参数签名
    def getSign(self, token, query):
        if isinstance(query, dict):
            query = params2str(query)
        resp = requests.post(SIGN_API + "/sign", json={"token": token, "query": query}).json()
        # print("签名返回: " + str(resp))
        sign = resp['data']
        return sign