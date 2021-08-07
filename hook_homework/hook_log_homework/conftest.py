from typing import List


# 改写编码格式，支持中文
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')  # 用例名字
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')  # 用例路径
