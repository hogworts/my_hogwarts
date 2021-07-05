from appium.webdriver.common.mobileby import MobileBy

from appium_project.appium_wx_delete_member_homework.page.base_page import BasePage


class MainPage(BasePage):
    _address_list_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def click_contact_button(self):
        # 点击通讯录
        self.find_and_click(*self._address_list_element)

        from appium_project.appium_wx_delete_member_homework.page.contact_page import ContactInfo
        return ContactInfo(self.driver)
