import unittest
import ddt
from lib.courseLib import CourseManage
import time

class CourseTest1(unittest.TestCase):
    cm = CourseManage()

    # 类级别的（只运行一次）
    @classmethod
    def setUpClass(cls):
        cls.cm.login("auto","sdfsdfsdf")
        print('begin-所有用例执行前====我调用了\n')

    # 类级别的（只运行一次）
    @classmethod
    def tearDownClass(cls):
        print('end-所有用例执行后====我调用了')

    #测试用例1
    def test_101(self):
        dictBody = self.cm.add('大学语文' + str(int(time.time() * 100)), '', '1')
        # print(dictBody)
        self.assertEqual(dictBody["retcode"], 0, '测试失败')

    #测试用例3
    def test_103(self):
        print('执行了测试用例1-3方法')
        self.assertEqual(1,1,'失败的原因')

    #测试用例2
    # @unittest.skip('不执行的原因')
    def test_102(self):
        print('执行了测试用例1-2方法')
        self.assertEqual(1, 1, '失败的原因')





