import allure
import pytest

from po_homework.po.main_page import MainPage


@allure.feature("添加部门")
@allure.title("添加部门")
class TestAddDept:
    def setup(self):
        self.main = MainPage()

    @pytest.mark.parametrize("name", ["00技术部", "00财务部00", "00运营部00"], ids=["00技术部", "00财务部", "00运营部"])
    @allure.title("添加部门")
    def test_add_dept(self, name):
        # 添加部门，检查添加部门是否成功
        result = self.main.click_contact_span().click_add_dept().add_dept(name).get_dept_element()
        assert name == result

    def teardown(self):
        self.main.close_driver()
