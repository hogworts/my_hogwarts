import os
import time

from selenium.webdriver.common.by import By

from po_homework.po.base_page import BasePage
import allure, logging


class MainPage(BasePage):
    _CONTACT_BUTTON = (By.CSS_SELECTOR, "#menu_contacts>span")

    def click_contact_span(self):
        time.sleep(1)
        # 点击通讯录tab页签按钮
        from po_homework.po.contact_page import ContactPage
        with allure.step("点击通讯按钮"):
            logging.info("点击通讯录按钮")
            self.find_to_click(*self._CONTACT_BUTTON)
            logging.info("进入通讯录界面后截屏")
            contact_png = os.path.join(self.image_dir, 'contact_page.png')
            self.driver.get_screenshot_as_file(contact_png)
            # 存放报告中
            allure.attach.file(source=contact_png, name="进入通讯录界面截屏", attachment_type=allure.attachment_type.PNG)
        return ContactPage(self.driver)
