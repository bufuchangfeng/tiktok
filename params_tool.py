from urllib.parse import urlparse

# 拼装参数
def params2str(params):
    """
    :param params:{'ac': 'wifi', 'app_name': 'aweme'}
    :return:"ac=wifi&app_name=aweme"
    """
    query = ""
    for k, v in params.items():
        query += "%s=%s&" % (k, v)
    query = query.strip("&")
    return query


# 从url提取参数
def str2params(url):
    """
    :param url:"https://aweme.snssdk.com/aweme/v1/user/?ac=wifi&app_name=aweme"
    :return:{'ac': 'wifi', 'app_name': 'aweme'}
    """
    params = {}
    url_change = urlparse.urlparse(url)
    for item in url_change.query.split('&'):
        key, value = item.split('=')
        params[key] = value
    return params