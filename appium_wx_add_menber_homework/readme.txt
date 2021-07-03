'''
使用appium自动化添加联系人
1，点击【通讯录】
2，点击【添加成员】
3，点击【手动输入添加】
4，输入姓名
5，输入手机号
6，点击【保存】
'''

分析：
采用po思想，对本次作业进行封装，分化管理

1、启动app，进入到消息页面，在消息页面，点击通讯录，---po.message_page，return contact_page 中的对象
2、在通讯页面点击 “添加成员”，进入到 选择添加成员的方式页面。----，contact_page页面，return add_member_method_page页面对象
3、在选择添加方式页面，点击手动输入添加，进入到add_member_page页面，进行添加成员，添加成功后，返回到通讯录界面 return contact_page对象
4、在contact_page界面进行断言。toast断言，添加成员名称断言



定义一个base_page:
1、避免一个页面进行webdriver初始化
2、通过base_page进行webdriver对象的透传
3、各个页面进行继承，隔离变化，从而得到复用，增强代码灵活度

增加testcase机制
1、添加用例管理机制，易于维护

配合allure进行报告完善