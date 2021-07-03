from appium.webdriver.common.mobileby import MobileBy
from appium_project.appium_wx_add_menber_homework.po.base_page import BasePage


class AddMemberMethodPage(BasePage):
    __METHOD_BUTTON = (MobileBy.ID, "com.tencent.wework:id/che")
    __TOAST_INFO = (MobileBy.XPATH, '//*[@class="android.widget.Toast" and @text="添加成功"]')

    def choice_method_by_manual(self):
        """
        在选择添加成员方式界面，选择添加成员方式，后进入到添加成员的编辑界面
        :return: 返回添加成员的编辑界面对象
        """
        from appium_project.appium_wx_add_menber_homework.po.add_member_page import AddMemberPage

        # 选择手动添加按钮，进入到编辑添加成员界面
        self.info("选择手动添加按钮")
        self.wait_find(self.__METHOD_BUTTON).click()
        return AddMemberPage(self.driver)

    def get_toast(self):
        '''
          <android.widget.Toast index="1" package="com.android.settings" class="android.widget.Toast" text="添加成功" checkable="false" checked="false" clickable="false" enabled="false" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][0,0]" displayed="false" />

        :return:
        '''

        res = self.find(*self.__TOAST_INFO)
        if res:
            return True
        return False

    def back(self):
        self.driver.back()
