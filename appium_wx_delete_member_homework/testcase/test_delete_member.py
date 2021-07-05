import pytest
from hamcrest import *

from appium_project.appium_wx_delete_member_homework.page.app import App


class TestDeleteMember:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.startapp().goto_main()

    def teardown(self):
        self.app.back(5)

    def teardown_class(self):
        self.app.quit()

    @pytest.mark.parametrize("name", ["lily"])
    def test_delete_member(self, name):
        res = self.main.click_contact_button().click_member_by_name(name).click_setting_button().click_edit_member() \
            .click_delete_button().find_name_of_delete(name)

        assert len(res) == 0
