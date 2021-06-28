from selenium.webdriver.common.by import By

from po_homework.po.base_page import BasePage
import logging, os, allure


class ContactPage(BasePage):
    _ADD_BUTTON = (By.CSS_SELECTOR, "i.member_colLeft_top_addBtn")
    _ADD_DEPT_BUTTON = (By.CSS_SELECTOR,
                        'ul[class="vakata-context jstree-contextmenu jstree-default-contextmenu js_create_dropdown_container"] li:nth-child(1)')

    @allure.title("添加部门")
    def click_add_dept(self):
        from po_homework.po.dept_page import DeptPage
        with allure.step("点击+号"):
            # 在通讯录页面，点击+号
            logging.info("点击加号，添加部门")
            self.wait_find(self._ADD_BUTTON).click()
            add_dept_button = os.path.join(self.image_dir, 'add_button.png')
            logging.info("点击添加部门按钮后，截图")
            self.driver.get_screenshot_as_file(add_dept_button)
            allure.attach.file(source=add_dept_button, name="点击+号的截屏", attachment_type=allure.attachment_type.PNG)

        with allure.step("选择'添加部门'选项"):
            # 点击添加部门,进入到添加部门页面
            logging.info("点击添加部门选项")
            self.wait_find(self._ADD_DEPT_BUTTON).click()

        return DeptPage(self.driver)
