from homework_api.api_core.api_function import Contact
import pytest
import allure
import yaml
import sys
import os

homework_api_path = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, homework_api_path)


@allure.feature("微信通讯录增删查改基础功能测试")
class TestContactApi:
    def setup(self):
        self.contact = Contact()

    def teardown(self):
        pass

    @allure.story("添加成员")
    @allure.title("添加成员")
    @pytest.mark.parametrize("dict_kwargs",
                             yaml.safe_load(open("./test_data.yml", encoding="utf-8")))
    def test_add_contact(self, dict_kwargs):
        res = self.contact.add_contact(dict_kwargs)
        assert res.json()["errcode"] == 0
        assert res.json()["errmsg"] == 'created'

    @allure.story("更新成员")
    @allure.title("更新成员")
    @pytest.mark.parametrize("dict_kwargs", yaml.safe_load(open("./test_data.yml", encoding="utf-8")))
    def test_update_contact(self, dict_kwargs):
        res = self.contact.update_contact(dict_kwargs)
        assert res.json()["errcode"] == 0
        assert res.json()["errmsg"] == "updated"

    @allure.story("获取成员")
    @allure.title("获取成员")
    @pytest.mark.parametrize("dict_kwargs", yaml.safe_load(open("./test_data.yml", encoding="utf-8")),
                             ids=["第1个", "第2个", "第3个"])
    def test_get_contact(self, dict_kwargs):
        res = self.contact.get_contact(dict_kwargs)
        assert res.json()["userid"] == dict_kwargs["userid"]
        assert res.json()["errcode"] == 0

    @allure.story("删除成员")
    @allure.title("删除成员")
    @pytest.mark.parametrize("dict_kwargs", yaml.safe_load(open("./test_data.yml", encoding="utf-8")),
                             ids=["第1个", "第2个", "第3个"])
    def test_delete_contact(self, dict_kwargs):
        res = self.contact.delete_contact(dict_kwargs)
        assert res.json()["errcode"] == 0
        assert res.json()["errmsg"] == "deleted"
