from lib.courseLib import CourseManage
import time
"""
测试用例1：新增课程
"""
#1-对象实例化
cm=CourseManage()
#2-对象调用实例方法login，子类对象调用父类方法，进行登录
cm.login('auto','sdfsdfsdf')

#3-对象调用实例方法add,进行课程新增，返回的的字典格式的消息体
dictBody=cm.add('大学语文2222'+str(int(time.time()*100)),'','1')
print(dictBody)

#4-断言的方式判断retcode=0
assert dictBody['retcode']==5
print(">>>>>>测试用例执行成功")

#5-if 的方式判断retcode=0
if dictBody['retcode']==0:
    print(">>>>>>测试用例执行成功")


