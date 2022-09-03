# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/3/13

import unittest
import MySQLdb



class TestCalssA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        "连接数据库，做数据初始化操作"


    def testAdd(self):
        assert 1==1

    @classmethod
    def tearDownClass(cls):
        "连接数据库，做数据清理的操作"
        # 打开数据库连接
        db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", port=3306, db="plesson", charset="utf8")

        # 获取操作游标
        cu = db.cursor()
        # 构造sql语句
        sql = """
        delete from sq_course
        where name like '课程%';
        """
        # 执行sql语句
        cu.execute(sql)
        sql = """
        delete from sq_course
        where name like 'sql课程%';
        """
        # 执行sql语句
        cu.execute(sql)
        # 提交数据库修改
        db.commit()
        print("删除成功")
        # 释放资源
        cu.close()
        db.close()

if __name__ == '__main__':
    # # 测试加载器
    # lo = unittest.TestLoader()
    # # 测试组
    # suite = unittest.TestSuite()
    # # 从测试类加载测试用例
    # tests = lo.loadTestsFromTestCase(TestCalssA)
    # # 把测试用例加到测试组
    # suite.addTests(tests)
    # # 运行测试组
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # unittest.defaultTestLoader.discover()

    unittest.main()
