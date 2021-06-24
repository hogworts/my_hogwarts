import pytest
import logging
from pytest_homework02.feature.calc_function import Calc


@pytest.fixture(scope="function", autouse=True)
def calc():
    logging.info("开始计算")
    calc = Calc()
    yield calc
    logging.info("结束计算")
