import time
import logging, os
import allure
from selenium.webdriver.common.by import By
from po_homework.po.base_page import BasePage


@allure.feature("部门管理")
class DeptPage(BasePage):
    _DEPT_NAME = (By.CSS_SELECTOR, 'form.form input[name="name"]')
    _Department = (By.CSS_SELECTOR, 'form.form a[class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]')
    _choice_dept = (By.CSS_SELECTOR, '.qui_dialog_body li[role="treeitem"] .jstree-anchor')
    _submit_button = (By.XPATH, '//a[@d_ck="submit"]')
    _check_name = (By.CSS_SELECTOR, 'div.member_colRight #party_name')

    @allure.title("添加部门信息")
    def add_dept(self, name):
        # 输入部门名称
        with allure.step("输入部门名称"):
            logging.info("输入部门名称")
            self.wait_find(self._DEPT_NAME).send_keys(name)

        # 选择所属部门
        with allure.step("选择部门"):
            logging.info("选择所属部门")
            self.wait_find(self._Department).click()
            self.finds(*self._choice_dept)[1].click()
            dept_info_picture = os.path.join(self.image_dir, "dept_info.png")
            self.driver.get_screenshot_as_file(dept_info_picture)
            allure.attach.file(source=dept_info_picture, name="填入部门信息", attachment_type=allure.attachment_type.PNG)

        # 点击确定按钮
        with allure.step("点击保存"):
            logging.info("点击保存按钮")
            self.find_to_click(*self._submit_button)
        return DeptPage(self.driver)

    def get_dept_element(self):
        time.sleep(1)
        ele = self.find(*self._check_name)
        return ele.text
