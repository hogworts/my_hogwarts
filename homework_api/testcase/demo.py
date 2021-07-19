info_list = [{
    "userid": "test1",
    "name": "test1",
    "department": [0],
    "email": "test1@163.com",
},
    {
        "userid": "test2",
        "name": "test2",
        "department": [0],
        "email": "test2@163.com",
    },
    {
        "userid": "test3",
        "name": "test3",
        "department": [0],
        "email": "test3@163.com",
    }
]

import yaml

# with open("test_data.yml", "w+", encoding="utf-8")as fw:
#     yaml.safe_dump(info_list, fw)

res = yaml.safe_load(open("./test_data.yml", encoding="utf-8"))
print(res)
print(type(res))
