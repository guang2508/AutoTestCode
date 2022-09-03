# -*- coding: utf-8 -*-

#测试文件以test_开头（或以_test结尾）
#测试文件以Test开头，并且不能带有init方法
#测试函数以test_开头
#断言使用基本的assert即可

import pytest

class Testcase:
    #一个test_函数是一条用例
    def test_01(self):
        print('这个是第一条用例')
        assert 1=='1'
