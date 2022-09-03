import MySQLdb

##-------------------查询----------------------
#打开数据库连接
# db=MySQLdb.connect(host="192.168.0.117",user="songqin",passwd="songqin",
#                    db="plesson",port=3306,charset="utf8")
# #获取操作游标
# cu=db.cursor()
# #执行sql
# cu.execute("select * from plesson.sq_course")
# #获取执行结果fetchone:获取一个   fetchall：获取所有    结果为：元祖
# data=cu.fetchall()
# print(data)
# #关闭，释放资源
# cu.close()
# db.close()

# ##-------------------增加-----------------------
db=MySQLdb.connect(host="192.168.0.117",user="songqin",passwd="songqin",
                   port=3306,db="plesson",charset="utf8")
#获取操作游标
cu=db.cursor()
#sql语句
sql='''
INSERT INTO plesson.sq_course(id,`name`,`desc`,display_idx) VALUES 
(5,'c#','c#课程学习',5),
(4,'java','java课程',4)
'''
#执行sql语句
cu.execute(sql)
#提交到数据库
db.commit()
#获取执行结果
data=cu.fetchall()
#关闭释放资源
cu.close()
db.close()

##--------------------改------------------------
#打开数据库
# db=MySQLdb.connect(host="192.168.0.117",user="songqin",passwd="songqin",port=3306,
#                    db="plesson",charset="utf8")
# #获取操作游标
# cu=db.cursor()
# #sql语句
# sql='''
# update plesson.sq_course set `desc`='pyrhon基础课' where id=1
# '''
# #执行sql语句
# cu.execute(sql)
# #提交到数据库
# db.commit()
# #获取结果
# data=cu.fetchall()
# print(data)
# #关闭释放资源
# cu.close()
# db.close()