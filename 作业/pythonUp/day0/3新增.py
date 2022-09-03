# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/3/13

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", port=3306, db="plesson", charset="utf8")

# 获取操作游标
cu = db.cursor()

# # 构造sql语句
# sql = """
# insert into sq_course
# VALUES (7, '课程3', '这是课程3的描述', 1)
# """


# 一次性插入多条数据
sql = """
insert into sq_course(name, `desc`, display_idx)
values ('sql课程1', 'sql课程1描述', 1),
       ('sql课程2', 'sql课程2描述', 1),
       ('sql课程3', 'sql课程3描述', 1),
       ('sql课程4', 'sql课程4描述', 1),
       ('sql课程5', 'sql课程5描述', 1);
"""

# 执行SQL
cu.execute(sql)
# 但凡涉及到数据库数据修改的都需要提交  insert delete update
db.commit()
# 获取返回值
data = cu.fetchall()
print("data =", data)

cu.close()
db.close()

