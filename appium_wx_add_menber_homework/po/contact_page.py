import allure
from appium.webdriver.common.mobileby import MobileBy

from appium_project.appium_wx_add_menber_homework.po.base_page import BasePage
import os


class ContactPage(BasePage):
    __ADD_MEMBER_BUTTON = (MobileBy.XPATH,
                           '//*[@resource-id="com.tencent.wework:id/dfd"]//android.widget.TextView[@text="添加成员"]')

    def click_add_member_button(self):
        """
        在通讯录页面点击，添加成员按钮，后，进入到选择添加成员方式页面
        :return:返回添加成员方式页面对象
        """
        from appium_project.appium_wx_add_menber_homework.po.add_member_method_page import AddMemberMethodPage
        # 在通讯录界面，选择添加成员,进入选择添加成员方式界面,,采用滚动方式查找，以防用户很多的时候，需要查找
        # self.find(*self.__ADD_MEMBER_BUTTON).click()
        self.info("开始滚动查找添加成员按钮，并点击")
        self.find_by_scroll().click()
        method_image = os.path.join(self.image_path, "choice_method_image.png")
        self.driver.get_screenshot_as_file(method_image)
        self.info("开始截图")
        allure.attach.file(source=method_image, name="选择添加成员方式界面", attachment_type=allure.attachment_type.PNG)

        return AddMemberMethodPage(self.driver)
