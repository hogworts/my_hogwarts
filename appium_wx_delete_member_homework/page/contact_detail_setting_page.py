from appium.webdriver.common.mobileby import MobileBy

from appium_project.appium_wx_delete_member_homework.page.base_page import BasePage


class ContactDetailSetting(BasePage):
    _edit_button = (MobileBy.XPATH, '//*[@text="编辑成员"]')

    def click_edit_member(self):
        self.find_and_click(*self._edit_button)

        from appium_project.appium_wx_delete_member_homework.page.contact_edit_page import ContactEditPage
        return ContactEditPage(self.driver)
