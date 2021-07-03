from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
import os


class BasePage:
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'image')

    def __init__(self, base_driver: WebDriver = None):
        # 如果还没有driver就初始化一次，如果有就复用传进来的driver
        if base_driver is None:
            desire_capability = {
                "platformName": "Android",
                "platformVersion": "7.1.2",
                "automationName": "UiAutomator2",
                "deviceName": "127.0.0.1:62001",
                "appPackage": " com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": True,
                "skipDeviceInitialization": "true",  # 省去设备的初始化的动作，提高速度
                # 应对中文
                "unicodeKeyboard": "true",
                "resetKeyboard": "true"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_capability)
            self.driver.implicitly_wait(10)
        else:
            self.driver = base_driver

    def find(self, by, locator) -> WebElement:
        ele: WebElement = self.driver.find_element(by, locator)
        return ele

    def finds(self, by, locator) -> list:
        eles: list = self.driver.find_elements(by, locator)
        return eles

    def wait_find(self, locator: tuple):
        ele: WebElement = WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable(locator))
        return ele

    def find_by_scroll(self):
        ele: WebElement = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                                   'new UiScrollable(new UiSelector().scrollable(true).\
                                                   instance(0)).scrollIntoView(new UiSelector().\
                                                   text("添加成员").instance(0));')

        return ele

    def info(self, comment):
        return logging.info(comment)

    def close_driver(self):
        self.driver.quit()
