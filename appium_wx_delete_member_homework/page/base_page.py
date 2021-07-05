from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def log_info(self, comment):
        logging.info(comment)

    def find(self, by, locator):
        self.log_info("find")
        self.log_info(by)
        self.log_info(locator)
        ele: WebElement = self.driver.find_element(by, locator)
        return ele

    def find_and_click(self, by, locator):
        self.log_info("find_and_click")
        self.log_info(by)
        self.log_info(locator)
        self.find(by, locator).click()

    def find_and_sentkeys(self, by, locator, text):
        self.log_info("find_and_sentkeys")
        self.log_info(by)
        self.log_info(locator)
        self.find(by, locator).send_keys(text)

    def get_toast_text(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result

    def back(self, num=3):
        for i in range(num):
            self.driver.back()

    def swipe_find(self, text, max_swipe_count=5):
        count = 0
        while count <= max_swipe_count:
            try:
                # 如果找到了元素，就返回
                self.log_info("找元素")
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return element

            # 如果没找到元素，就开始滑动找
            except NoSuchElementException:
                self.log_info("获取窗口大小")
                # 获取窗口的高宽，返回字典return {k: size[k] for k in ('width', 'height')}
                size = self.driver.get_window_size()
                # 取出高，宽
                width = size.get("width")
                height = size.get("height")

                # 滑动，找元素,X轴一般不变，取窗口的中间，从下往上滑动。下：整个窗口高度的4/5，上：整个窗口高度的1/5
                # duration:表示滑动的速度，一般设定2s，越慢越准确
                self.log_info(f"开始第{count}次滑动")
                self.driver.swipe(start_x=width / 2, start_y=height * 0.8, end_x=width / 2, end_y=height * 0.3,
                                  duration=2000)
                count += 1

            if count == max_swipe_count:
                raise NoSuchElementException(f"找了{max_swipe_count}次，没找到元素")
