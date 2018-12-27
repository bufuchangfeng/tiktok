import json
import time
import api
from sign import Sign
from config import CONFIG


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
            print('=' * 20)

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
            print('=' * 20)

            if resp['has_more'] == False or len(resp['followers']) == 0 or len(
                    out_data['followers']) >= target_count:
                return

        # 默认30s。如果丢失数据可缩小秒数。如果数据重复可增加秒数。
        next_max_time = resp.get('min_time', int(time.time())) - 30
        get_out_data(next_max_time)

    get_out_data()
    return json.dumps(out_data)


def main():
    pass


if __name__ == '__main__':
    main()
