#-*- coding: utf-8 -*-
#@File    : handle_yml.py
#@Time    : 2021/11/12 21:31
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/12 
#安装库 pip install PyYaml
import yaml
def get_yaml_data(fileDir):
    """
    :param fileDir: 文件的路径
    :return: 返回yaml内容
    """
    #1- 文件在磁盘----open函数---在内存去打开
    with open(fileDir,encoding='utf-8') as fo:#fo 文件对象
        return yaml.safe_load(fo.read())#使用yaml加载方法去得到文件里内容


#获取yaml用例的函数
def get_yaml_caseData(fileDir):
    resList = []# 存放结果[(标题，请求数据，响应数据),()]
    res = get_yaml_data(fileDir)
    for one in res:
        resList.append((one['detail'],one['data'],one['resp']))
    return resList
    #出来读取出的数据---[(标题，请求数据，响应数据),()]

if __name__ == '__main__':
    #TODO 以后注意修改成 工程的绝对路径-2021.xx.xx
    res = get_yaml_data('../data/songqin.yml')
    print(res)