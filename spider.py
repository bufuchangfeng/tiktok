import json
import time
import api
from sign import Sign
import requests
from config import CONFIG

device_info = Sign().getDevice()

common_params = {
            "iid": device_info['iid'],
            "idfa": device_info['idfa'],
            "vid": device_info['vid'],
            "device_id": device_info['device_id'],
            "openudid": device_info['openudid'],
            "device_type": device_info['device_type'],
            "os_version": device_info['os_version'],
            "os_api": device_info['os_api'],
            "screen_width": device_info['screen_width'],
            "device_platform": device_info['device_platform'],
            "version_code": CONFIG['APPINFO']['version_code'],
            "channel": CONFIG['APPINFO']['channel'],
            "app_name": CONFIG['APPINFO']['app_name'],
            "build_number": CONFIG['APPINFO']['build_number'],
            "app_version": CONFIG['APPINFO']['app_version'],
            "aid": CONFIG['APPINFO']['aid'],
            "ac": "WIFI",
            "pass-region": "1",  # new
            # "js_sdk_version": "1.3.0.1"
}

token = Sign().getToken()


def user_detail(user_id):
    url, extra_params = api.user(user_id=user_id)
    params = dict(common_params, **extra_params)

    # 参数加签（* 要对全部参数加签 *）
    sign = Sign().getSign(token, params)
    params["mas"] = sign['mas']
    params["as"] = sign['as']
    params["ts"] = sign['ts']

    resp = requests.get(url, params=params, headers=CONFIG['HEADER']).json()
    print(json.dumps(resp))

    data = resp['user']
    out_data = {
        'user_id': data['uid'],
        'nickname': data['nickname'],
        'signature': data['signature'],
        'sex': data['gender'],
        'address': data['country'] + data['city'] + data['district'],
        'constellation': data['constellation'],
        'avatar': data['avatar_larger']['url_list'],
        'url': data['share_info']['share_url'],
        'follower_count': data['follower_count'],  # 粉丝数
        'total_favorited': data['total_favorited'],  # 获赞数
        'following_count': data['following_count'],  # 关注数
        'aweme_count': data['aweme_count'],  # 作品数
        'dongtai_count': data['dongtai_count'],  # 动态数
    }

    return json.dumps(out_data)


# 关注的用户
def user_followings(target_user_id, target_count=100):
    out_data = {
        'user_id': target_user_id,
        'followings': []
    }

    def get_out_data(max_time=int(time.time())):
        url, extra_params = api.following(user_id=target_user_id, count=20, max_time=max_time)
        params = dict(common_params, **extra_params)

        # 参数加签（* 要对全部参数加签 *）
        sign = Sign().getSign(token, params)
        params["mas"] = sign['mas']
        params["as"] = sign['as']
        params["ts"] = sign['ts']

        resp = requests.get(url, params=params, headers=CONFIG['HEADER']).json()
        print(json.dumps(resp))

        data = resp['followings']
        for item in list(data):
            item_data = {
                'user_id': item['uid'],
                'nickname': item['nickname']
            }
            if item_data not in out_data['followings']:
                out_data['followings'].append(item_data)

            print('%s/%s' % (len(out_data['followings']), resp['total']))

            if resp['has_more'] == False or len(resp['followings']) == 0 or len(
                    out_data['followings']) >= target_count:
                return

        # 默认30s。如果丢失数据可缩小秒数。如果数据重复可增加秒数。
        next_max_time = resp.get('min_time', int(time.time())) - 30
        get_out_data(next_max_time)

    get_out_data()
    return json.dumps(out_data)


# 用户的粉丝
def user_followers(target_user_id, target_count=100):
    out_data = {
        'user_id': target_user_id,
        'followers': []
    }

    def get_out_data(max_time=int(time.time())):
        url, extra_params = api.follower(user_id=target_user_id, count=20, max_time=max_time)
        params = dict(common_params, **extra_params)

        # 参数加签（* 要对全部参数加签 *）
        sign = Sign().getSign(token, params)
        params["mas"] = sign['mas']
        params["as"] = sign['as']
        params["ts"] = sign['ts']

        resp = requests.get(url, params=params, headers=CONFIG['HEADER']).json()
        print(json.dumps(resp))

        print(resp['total'])

        data = resp['followers']
        for item in list(data):
            item_data = {
                'user_id': item['uid'],
                'nickname': item['nickname']
            }
            if item_data not in out_data['followers']:
                out_data['followers'].append(item_data)

            print('%s/%s' % (len(out_data['followers']), resp['total']))

            if resp['has_more'] == False or len(resp['followers']) == 0 or len(
                    out_data['followers']) >= target_count:
                return

        # 默认30s。如果丢失数据可缩小秒数。如果数据重复可增加秒数。
        next_max_time = resp.get('min_time', int(time.time())) - 30
        get_out_data(next_max_time)

    get_out_data()
    return json.dumps(out_data)


def main():
    detail = json.loads(user_detail('99247509232'))

    print(detail['following_count'])

    user_followings('99247509232', detail['following_count'])
    pass


if __name__ == '__main__':
    main()
