import time


def following(user_id, count=20, max_time=int(time.time())):
    url = 'https://aweme.snssdk.com/aweme/v1/user/following/list/'
    extra_params = {
        "user_id": user_id,
        "count": str(count),
        "source_type": "2",
        "max_time": str(int(max_time)),
    }
    return url, extra_params


def follower(user_id, count=20, max_time=int(time.time())):
    url = 'https://aweme.snssdk.com/aweme/v1/user/follower/list/'
    extra_params = {
        "user_id": user_id,
        "count": str(count),
        "source_type": "2",
        "max_time": str(max_time),
    }
    return url, extra_params

