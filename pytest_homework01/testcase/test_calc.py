import logging

import allure
import pytest
from pytest_homework01.feature.calc_function import Calc
from pytest_homework01.tools.load_yaml_data import LoadData


@allure.feature("我的计算器")
class TestCalc:

    @allure.title("初始化被测类")
    def setup_class(self):
        self.calc = Calc()

    @allure.title("开始标记")
    def setup(self):
        logging.info("开始计算")

    @allure.title("结束标记")
    def teardown(self):
        logging.info("结束计算")

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["add_int"])
    @allure.story("int类型数据相加")
    @allure.title("int类型数据相加")
    def test_add_int(self, a, b, target):
        with allure.step("开始计算%s+%s" % (a, b)):
            assert target == self.calc.add_func(a, b)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["add_float"])
    @allure.story("float类型数据相加")
    def test_add_float(self, a, b, target):
        with allure.step("开始计算%s+%s" % (a, b)):
            assert target == self.calc.add_func(a, b)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["sub_int"])
    @allure.story("int类型数据相减")
    def test_sub_int(self, a, b, target):
        with allure.step("开始计算%s-%s" % (a, b)):
            logging.info("开始计算%s-%s" % (a, b))
            assert target == self.calc.sub_func(a, b)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["sub_float"])
    @allure.story("float类型数据相减")
    def test_sub_float(self, a, b, target):
        with allure.step(r"开始计算%s-%s" % (a, b)):
            assert target == self.calc.sub_func(a, b)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["mul_float"])
    @allure.story("float类型数据相乘")
    def test_mul_float(self, a, b, target):
        with allure.step(r"开始计算%s * %s" % (a, b)):
            assert target == self.calc.mul_func(a, b)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["mul_int"])
    @allure.story("int 类型数据相减")
    def test_mul_int(self, a, b, target):
        with allure.step(r"开始计算%s-%s" % (a, b)):
            assert target == self.calc.mul_func(a, b)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["div_float"])
    @allure.story("float类型数据相除")
    def test_mul_float(self, a, b, target):
        with allure.step(r"开始计算%s / %s" % (a, b)):
            assert target == self.calc.div_func(a, b)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["div_int"])
    @allure.story("int 类型数据相除")
    def test_mul_int(self, a, b, target):
        with allure.step(r"开始计算%s / %s" % (a, b)):
            assert target == self.calc.div_func(a, b)
