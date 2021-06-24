import logging

import allure
import pytest
from pytest_homework01.feature.calc_function import Calc
from pytest_homework01.tools.load_yaml_data import LoadData


@allure.feature("我的计算器")
class TestCalc:
    #
    # @allure.title("初始化被测类")
    # def setup_class(self):
    #     self.calc = Calc()
    #
    # @allure.title("开始标记")
    # def setup(self):
    #     logging.info("开始计算")
    #
    # @allure.title("结束标记")
    # def teardown(self):
    #     logging.info("结束计算")

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["add_int"])
    @allure.story("int类型数据相加")
    @allure.title("int类型数据相加")
    def test_add_int(self, a, b, target, calc):
        with allure.step("开始计算%s+%s" % (a, b)):
            assert target == calc.add_func(a, b)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["add_float"])
    @allure.story("float类型数据相加")
    @allure.title("float类型数据相加")
    def test_add_float(self, a, b, target, calc):
        with allure.step("开始计算%s+%s" % (a, b)):
            assert target == calc.add_func(a, b)
            allure.attach.file(source=r"./tupian.jpg", name="测试截图",
                               attachment_type=allure.attachment_type.JPG)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["sub_int"])
    @allure.story("int类型数据相减")
    @allure.title("int类型数据相减")
    def test_sub_int(self, a, b, target, calc):
        with allure.step("开始计算%s-%s" % (a, b)):
            logging.info("开始计算%s-%s" % (a, b))
            assert target == calc.sub_func(a, b)
            logging.info("开始插入图片")
            allure.attach.file(source=r"./tupian.jpg", name="测试截图",
                               attachment_type=allure.attachment_type.JPG)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["sub_float"])
    @allure.story("float类型数据相减")
    @allure.title("float类型数据相减")
    def test_sub_float(self, a, b, target, calc):
        with allure.step(r"开始计算%s-%s" % (a, b)):
            assert target == calc.sub_func(a, b)
            allure.attach.file(source=r"./tupian.jpg", name="测试截图",
                               attachment_type=allure.attachment_type.JPG)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["mul_float"])
    @allure.story("float类型数据相乘")
    @allure.title("float类型数据相乘")
    def test_mul_float(self, a, b, target, calc):
        with allure.step(r"开始计算%s * %s" % (a, b)):
            assert target == calc.mul_func(a, b)
            allure.attach.file(source=r"./tupian.jpg", name="测试截图",
                               attachment_type=allure.attachment_type.JPG)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["mul_int"])
    @allure.story("int 类型数据相减")
    @allure.title("int 类型数据相减")
    def test_mul_int(self, a, b, target, calc):
        with allure.step(r"开始计算%s-%s" % (a, b)):
            assert target == calc.mul_func(a, b)
            allure.attach.file(source=r"./tupian.jpg", name="测试截图",
                               attachment_type=allure.attachment_type.JPG)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["div_float"])
    @allure.story("float类型数据相除")
    @allure.title("float类型数据相除")
    def test_mul_float(self, a, b, target, calc):
        with allure.step(r"开始计算%s / %s" % (a, b)):
            assert target == calc.div_func(a, b)
            allure.attach.file(source=r"./tupian.jpg", name="测试截图",
                               attachment_type=allure.attachment_type.JPG)

    @pytest.mark.parametrize("a,b,target", LoadData().yaml_data()["div_int"])
    @allure.story("int 类型数据相除")
    @allure.title("int 类型数据相除")
    def test_mul_int(self, a, b, target, calc):
        # with allure.step(r"开始计算%s / %s" % (a, b)):
        logging.info("开始计算")
        with pytest.raises(ZeroDivisionError, ValueError, EOFError):
            assert target == calc.div_func(a, b)
        logging.info("开始截图")
        allure.attach.file(source=r"./tupian.jpg", name="测试截图", attachment_type=allure.attachment_type.JPG)
        logging.info("结束截图")
        logging.info("结束计算")
