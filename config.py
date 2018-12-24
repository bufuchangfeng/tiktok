import random
import copy

SIGN_API = "https://api.appsign.vip:2688"

CONFIG_LIST = {
    "2.7.0": {
        "APPINFO": {
            "version_code": "2.7.0",
            "app_version": "2.7.0",
            "channel": "App Stroe",
            "app_name": "aweme",
            "build_number": "27014",
            "aid": "1128",
        },
        "HEADER": {
            "User-Agent": "Aweme/2.7.0 (iPhone; iOS 11.0; Scale/2.00)",
        },
        "TOKEN_API": SIGN_API + "/token/douyin/version/2.7.0",
        "DEVICE_API": SIGN_API + "/douyin/device/new/version/2.7.0"
    },
    "2.8.0": {
        "APPINFO": {
            "version_code": "2.8.0",
            "app_version": "2.8.0",
            "channel": "App Stroe",
            "app_name": "aweme",
            "build_number": "28007",
            "aid": "1128",
        },
        "HEADER": {
            "User-Agent": "Aweme/2.8.0 (iPhone; iOS 11.0; Scale/2.00)"
        },
        "TOKEN_API": SIGN_API + "/token/douyin/version/2.8.0",
        "DEVICE_API": SIGN_API + "/douyin/device/new"  # 这部分没写错，目前没有2.8.0版本的专用接口
    },
    "2.9.1": {
        "APPINFO": {
            "version_code": "2.9.1",
            "app_version": "2.9.1",
            "channel": "App Stroe",
            "app_name": "aweme",
            "build_number": "29101",
            "aid": "1128",
        },
        "HEADER": {
            "User-Agent": "Aweme/2.9.1 (iPhone; iOS 11.0; Scale/2.00)"
        },
        "TOKEN_API": SIGN_API + "/token/douyin/version/2.9.1",
        "DEVICE_API": SIGN_API + "/douyin/device/new"  # 这部分没写错，目前没有2.9.1版本的专用接口
    }
}

# 随机版本
CONFIG = copy.deepcopy(CONFIG_LIST[random.choice(CONFIG_LIST.keys())])

# 指定版本
# CONFIG = CONFIG_LIST['2.7.0']
