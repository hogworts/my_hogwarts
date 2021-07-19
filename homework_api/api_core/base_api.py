import requests


class BaseApi:
    corpid = "wwea628167ec27f8e8"
    corpsecret = r'bvxMJZJEeE-Hm_WhZLvbst-78sv4x3HPrChRZbnDEJo'
    BASE_URL = r' https://qyapi.weixin.qq.com/cgi-bin/'

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = f"gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        r = self.send("GET", url=url)
        return r.json()["access_token"]

    def send(self, method, url, **kwargs):
        url = self.BASE_URL + url

        return requests.request(method=method, url=url, **kwargs)


if __name__ == '__main__':
    res = BaseApi()
    print(res.get_token())
