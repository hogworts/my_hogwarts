from appium import webdriver

from appium_project.appium_wx_delete_member_homework.page.base_page import BasePage
from appium_project.appium_wx_delete_member_homework.page.main_page import MainPage


class App(BasePage):
    def startapp(self):
        if self.driver is None:
            print("第一次初始化driver")
            desire_capability = {
                "automationName": "UiAutomator2",
                "platformName": "Android",
                "platformVersion": "7.1.2",
                "deviceName": "yesheng",
                "udid": "127.0.0.1:62001",
                "appActivity": ".launch.WwMainActivity",
                "appPackage": "com.tencent.wework",
                "unicodeKeyboard": "true",
                "resetKeyboard": "true",
                "noReset": "true",
                # "skipDeviceInitialization": "true"
            }
            self.driver = webdriver.Remote(r"http://127.0.0.1:4723/wd/hub", desire_capability)
            self.driver.implicitly_wait(5)
        else:
            print("driver已经存在，复用")
            self.driver.launch_app()

        # 将自己返回，自己就是self.driver的session
        return self

    def restart(self, num=3):
        self.driver.close()
        # 指定appActivity的app应用启动 app_package: str, app_activity: str
        # self.driver.start_activity(app_package="com.tencent.wework", app_activity=".launch.WwMainActivity")
        # 帮我启动，当前建立连接session里面的app
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        # 进入主页 入口
        return MainPage(self.driver)







