from appium.webdriver.common.mobileby import MobileBy

from appium_project.appium_wx_delete_member_homework.page.base_page import BasePage


class ContactDetailBriefInfo(BasePage):
    _setting_button = (MobileBy.XPATH, '//*[@text="个人信息"]/../../../../../android.widget.LinearLayout[2]')

    def click_setting_button(self):
        self.find_and_click(*self._setting_button)

        from appium_project.appium_wx_delete_member_homework.page.contact_detail_setting_page import \
            ContactDetailSetting
        return ContactDetailSetting(self.driver)
