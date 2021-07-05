from appium.webdriver.common.mobileby import MobileBy

from appium_project.appium_wx_delete_member_homework.page.base_page import BasePage


class ContactEditPage(BasePage):
    _delete_button = (MobileBy.XPATH, '//*[@text="删除成员"]')
    _confirm_button = (MobileBy.XPATH, '//android.widget.FrameLayout//android.widget.TextView[@text="确定"]')

    def click_delete_button(self):
        # 滑动点击删除成员按钮
        self.swipe_find(text="删除成员", max_swipe_count=3).click()

        # 点击弹框的确定按钮
        self.find_and_click(*self._confirm_button)

        from appium_project.appium_wx_delete_member_homework.page.contact_page import ContactInfo
        return ContactInfo(self.driver)
