import os
import time

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

cookie_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "cookie_data.yml")


class BasePage:
    image_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "image")

    def __init__(self, base_driver: WebDriver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

            # 登录微信，获取token
            # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            # time.sleep(15)
            #
            # data = self.driver.get_cookies()
            # with open(cookie_file, "w", encoding="UTF-8") as f:
            #     yaml.safe_dump(data, f)

            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            with open(cookie_file, "r", encoding="utf-8") as f:
                datas = yaml.safe_load(f)

            for temp in datas:
                self.driver.add_cookie(temp)

            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self.driver = base_driver

    def find(self, by, locator) -> WebElement:
        """
        find_element_by
        :param by: By.ID,By.XPATH 等
        :param locator: 查找元素表达式
        :return: 返回一个element对象
        """
        ele: WebElement = self.driver.find_element(by, locator)
        return ele

    def finds(self, by, locator) -> list:
        """
        find_element_by
        :param by: By.ID,By.XPATH 等
        :param locator: 查找元素表达式
        :return: 返回一组element对象
        """
        eles = self.driver.find_elements(by, locator)
        return eles

    def find_to_click(self, by, locator):
        """
        find_element_by
        :param by: By.ID,By.XPATH 等
        :param locator: 查找元素表达式
        :return: 返回一组element对象
        """
        ele: WebElement = self.driver.find_element(by, locator)
        ele.click()

    def wait_find(self, locator, timeout=10) -> WebElement:
        """
        通过添加显式等待，进行元素的查找
        :param locator:示例 (By.ID,"su")
        :param timeout: 超时时间，默认10s
        :return: 返回一个element对象
        """
        ele: WebElement = WebDriverWait(self.driver, timeout, 0.5).until(EC.element_to_be_clickable(locator))
        return ele

    def close_driver(self):
        self.driver.quit()
