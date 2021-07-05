import time

from appium.webdriver.common.mobileby import MobileBy

from appium_project.appium_wx_delete_member_homework.page.base_page import BasePage


class ContactInfo(BasePage):

    def click_member_by_name(self, name):
        _locator = f'//*[@class ="android.widget.ListView"]//android.widget.RelativeLayout//android.widget.TextView[@text="{name}"]'

        print(_locator)
        time.sleep(5)

        self.find_and_click(MobileBy.XPATH, _locator)

        from appium_project.appium_wx_delete_member_homework.page.contact_detail_briefInfo_page import \
            ContactDetailBriefInfo
        return ContactDetailBriefInfo(self.driver)

    def find_name_of_delete(self, name):
        time.sleep(5)
        _locator = f'//*[@class ="android.widget.ListView"]//android.widget.RelativeLayout//android.widget.TextView[@text="{name}"]'

        res: list = self.driver.find_elements(MobileBy.XPATH, _locator)

        print(f"================={res}===============")
        return res
