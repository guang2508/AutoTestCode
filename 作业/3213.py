# -*- coding: utf-8 -*-

#try except语句中,至少要有一个except,也可以有多个.也可以加上一个else语句,一个finally语句
# try:
#	int1=int(input('请输入一个数字:	'))
#	print(1/int1)
# except ZeroDivisionError:	#0作为分母的异常
#	print('0不能作为分母')
# except ValueError:	#输入非数字的异常
#	print('您输入的不是数字')
# except:	#如果不指定异常类型,则捕获任何异常
#	print('程序出现错误')
# else:	#当程序没有捕获到任何异常,会执行else中的语句
#	print('没有出现异常')
# finally:	#无论程序有没有出现异常,都会执行
#	print('程序执行完毕')

#常见的异常
# NameError	#未定义的变量
# print(a)
# IndexError	#下标越界
# list1=[10]
# print(list1[1])
# FileNotFoundError	#找不到文件异常
# with open('./ojomomo.txt') as file1:
#	file1.read()

#所有的异常,都是Exception的子类,或者子类的子类,Exception也有一个父类	BaseException
# print(NameError.__base__)
# print(IndexError.__base__)
# print(LookupError.__base__)
# print(FileNotFoundError.__base__)
# print(OSError.__base__)
# print(Exception.__base__)

#手动抛出异常
# try:
#	raise IOError	#假装这里有异常
# except IOError:
#	print('程序出现了IO异常')

#日志
import time
import logging
import traceback
logging.basicConfig(level='DEBUG',filename='D:/log51.log',filemode='a+')
# logging.debug(1)
# logging.info(2)
# logging.warning(3)
# logging.error(4)
# logging.critical(5)

try:
    int1=int(input('请输入一个数字:	'))
    print(1/int1)
except ZeroDivisionError:	#0作为分母的异常
    logging.error(time.strftime('%y-%m-%d %H:%M:%S')+traceback.format_exc())
except ValueError:	#输入非数字的异常
    logging.error(time.strftime('%y-%m-%d %H:%M:%S')+traceback.format_exc())

#课堂小结
#try except else finally
#常见的异常
#手动抛出异常 raise
#logging模块,traceback