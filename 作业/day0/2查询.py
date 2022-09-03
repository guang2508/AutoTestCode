# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2020/3/13

import requests
import MySQLdb

def get_course_from_api():
    res = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
    return res.json()["retlist"]

def get_course_from_db():
    # 打开数据库连接
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", port=3306, db="plesson", charset="utf8")
    # 获取操作游标
    cu = db.cursor()
    # 构造sql语句
    sql = """
    select * 
    from sq_course;
    """
    try:
        # 执行SQL
        cu.execute(sql)
        # 获取返回值
        data = cu.fetchall()
    except:
        print("Error:unable to fecth data")
    #释放资源
    cu.close()
    db.close()
    return data

if __name__ == '__main__':
    dbData = get_course_from_db()
    apiData = get_course_from_api()
    for ele in dbData:
        print(list(ele))
    for ele in apiData:
        course_info = ["", "", "", ""]
        i = 0
        for key in ele:
            course_info[i] = ele[key]
            i += 1
        print(course_info)


# [{"a":"a"}, '课程1', '详细情况1', 1]
# ['课程1', {"a":"a"},  '详细情况1', 1]
# for i in list1:
#     try:
#         list2.remove(i)
#     except:
#         false
# if len(list2) > 0:false
# else:true

sli = []
for i in range(100):
    sli.append(i)
sli = [i for i in range(100)]
try:
    pass
except Exception as e:
    print(e)
