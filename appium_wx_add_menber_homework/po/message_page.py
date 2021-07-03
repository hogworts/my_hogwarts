import os
from appium.webdriver.common.mobileby import MobileBy
from appium_project.appium_wx_add_menber_homework.po.base_page import BasePage
import allure


class MessagePage(BasePage):
    __BUTTON_ELEMENT = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/e14" and @text="通讯录"]')

    def click_contact_button(self):
        """
        在消息页面，点击通讯录按钮，进入到通讯录页面
        :return: 通讯录页面对象
        """
        from appium_project.appium_wx_add_menber_homework.po.contact_page import ContactPage

        # 点击通讯录，进入到通讯录界面
        self.info("点击通讯录，进入到通讯录界面")
        self.find(*self.__BUTTON_ELEMENT).click()

        self.info("进入界面开始截屏")
        image_dir = os.path.join(self.image_path, "contact_image.png")
        self.driver.get_screenshot_as_file(image_dir)
        allure.attach.file(source=image_dir, name="进入通讯录界面截屏", attachment_type=allure.attachment_type.PNG)

        return ContactPage(self.driver)
