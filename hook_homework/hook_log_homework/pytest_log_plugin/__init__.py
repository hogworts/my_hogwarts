# 编写一个插件
# 创建一个日志的实例，定义好日志的格式，将日志保存到项目目录下的logs/ 目录下
# 改写编码格式，支持中文
# item.name = item.name.encode('utf-8').decode('unicode-escape')
# item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
# 打包
import logging

import os


def plugin_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if not os.path.exists('./logs'):  # 判断logs文件是否存在
        os.makedirs('./logs')

    log_path = "./logs/log.log"

    # 定义日志格式
    formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")  # 设置日志输出/打印格式

    # 创建文件handler
    fh = logging.FileHandler(log_path)
    fh.setLevel(logging.DEBUG)
    # 制定文件格式
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # 创建console-handler
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    # 制定console打印日志格式
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    return logger


logger = plugin_logger()
