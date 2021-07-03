import os

import allure
from appium.webdriver.common.mobileby import MobileBy

from appium_project.appium_wx_add_menber_homework.po.base_page import BasePage


class AddMemberPage(BasePage):
    __NAME_BUTTON = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b8t"]/android.widget.EditText')
    __PHONE_BUTTON = (MobileBy.XPATH,
                      '//*[@resource-id="com.tencent.wework:id/f85"]')

    __SAVE_BUTTON = (MobileBy.XPATH, '//*[@text="保存"]')

    def add_member(self, name, phone):
        """

        :param name: 输入姓名
        :param phone: 输入电话
        :return: 添加成员成功后，返回到通讯录页面
        """
        from appium_project.appium_wx_add_menber_homework.po.add_member_method_page import AddMemberMethodPage
        self.info("输入姓名")
        # 输入姓名
        self.wait_find(self.__NAME_BUTTON).send_keys(name)
        # 输入电话号码
        self.info("输入电话")
        self.find(*self.__PHONE_BUTTON).send_keys(phone)
        self.info("开始截屏")
        edit_image = os.path.join(self.image_path, "edit_image.png")
        self.driver.get_screenshot_as_file(edit_image)
        allure.attach.file(source=edit_image, name="添加成员截图", attachment_type=allure.attachment_type.PNG)

        # 点击保存按钮
        self.info("点击保存")
        self.find(*self.__SAVE_BUTTON).click()

        # print(self.driver.page_source)

        return AddMemberMethodPage(self.driver)
