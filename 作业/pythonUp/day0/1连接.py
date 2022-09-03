# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/3/13

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", port=3306, db="plesson")

# 获取操作游标
cu = db.cursor()

# 通过 execute 方法执行sql语句
cu.execute("select version();")

# 获取执行结果
data = cu.fetchone()  # 获取一条结果
# data = cu.fetchall()  # 获取所有
# data = cu.fetchmany(x)  # 获取 x 条记录

print("数据库版本是:", data)

# 释放资源
cu.close()
db.close()
