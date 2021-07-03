from hamcrest import *
import pytest, allure

from appium_project.appium_wx_add_menber_homework.po.message_page import MessagePage


@allure.feature("手动添加成员")
class TestAddMember:
    def setup(self):
        self.main = MessagePage()

    def teardown(self):
        self.main.close_driver()

    @pytest.mark.parametrize("name, phone", [("lily", "13678789898"),
                                             ("lily1", "13678789899"),
                                             ("lily2", "13678789896"),
                                             ("lily3", "13678789898"),
                                             ])
    @allure.story("微信添加成员")
    @allure.title("输入正常电话、姓名场景")
    def test_add_member(self, name, phone):
        # 链式调用
        res = self.main.click_contact_button().click_add_member_button() \
            .choice_method_by_manual().add_member(name, phone).get_toast()

        # assert res == True
        assert_that(res, equal_to(True))
