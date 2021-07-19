import time

from homework_api.api_core.base_api import BaseApi


class Contact(BaseApi):
    def add_contact(self, dict_kwargs: dict):
        """
        :param kwargs:userid,name,department,email
        :return: 返回添加的对象
        """
        add_url = f'user/create?access_token={self.token}'
        response = self.send(method="POST", url=add_url, json=dict_kwargs)
        print(response.text)
        return response

    def get_contact(self, dict_kwargs: dict):
        userid = dict_kwargs["userid"]
        url = f'user/get?access_token={self.token}&userid={userid}'
        response = self.send("GET", url)
        return response

    def update_contact(self, dict_kwargs: dict, **kwargs):
        """
        :param userid: 必填选项
        :return:
        """
        userid = dict_kwargs["userid"]
        name = dict_kwargs["name"] + str(time.time())
        url = f"user/update?access_token={self.token}"
        data = {"userid": userid,
                "name": name}
        data.update(kwargs)
        response = self.send("POST", url, json=data)
        return response

    def delete_contact(self, dict_kwargs: dict):
        userid = dict_kwargs["userid"]
        url = f'user/delete?access_token={self.token}&userid={userid}'
        response = self.send("GET", url)
        return response


if __name__ == '__main__':
    ctt = Contact()
    print(ctt.update_contact(userid="xixili", name="ceshi").text)
    data = {
        "userid": "test1",
        "name": "测试1",
        "department": [1],
        "email": "test1@163.com"
    }
    res = ctt.add_contact(**data)
    print(res.text)

    r = ctt.get_contact()
    print(r.text)
    print(ctt.delete_contact().text)
