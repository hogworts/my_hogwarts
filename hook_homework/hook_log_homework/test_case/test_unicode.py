import pytest
from hook_log_homework.pytest_log_plugin import logger


@pytest.mark.parametrize('name', ["西西里", "xixili", "西西里2"], ids=["西西里1", "xixili", "西西里2"])
def test_unicode(name):
    logger.info(name)
