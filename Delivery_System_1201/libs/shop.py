#-*- coding: utf-8 -*-
#@File    : shop.py
#@Time    : 2021/11/12 21:45
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/12 
from common.baseAPI import BaseAPI
from configs.config import NAME_PSW
from libs.login import Login
from utils.handle_path import testData_path
import os
class Shop(BaseAPI):
    #1- 列出店铺
    #2- 更新店铺
    pass
    """
    店铺更新接口：数据从用例文件去读取  excel/yaml
        1- id  需要代码里去更新--字典可以更新值
        2- 图片信息需要传入
    """
    def update(self,inData,shopID,fileInfo):
        if inData['id'] == 'id不存在':#u不更新
            inData['id'] = '0000'
        else:#1- 更新店铺id
            inData['id'] = shopID

        #2- 更新文件信息
        inData['image_path'] =fileInfo
        inData['image'] = f'/file/getImgStream?fileName={fileInfo}'
        return super(Shop,self).update(inData)#  调用父类的更新方法


if __name__ == '__main__':
    #1- 登录操作---获取token
    token = Login().login(NAME_PSW,getToken=True)
    print(token)
    #2- 创建店铺实例
    shop = Shop(token)
    #3- 列出店铺
    testData = {'page':1,'limit':20}
    res = shop.query(testData)
    print(res)
    #------获取店铺id-----
    shopID = res['data']['records'][0]['id']
    print('当前店铺的id>>> ',shopID)
    #4- 文件上传
    res2 = shop.file_upload(os.path.join(testData_path,'xintian.png'))
    print(res2)
    fileInfo = res2['data']['realFileName']
    print('图片信息>>> ', fileInfo)

    #5- 更新店铺
    shopData = {
            "name": "心田小卖部",
            "address": "上海市静安区秣陵路303号",
            "id": "3269",
            "Phone": "13176876632",
            "rating": "6.0",
            "recent_order_num":100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
        }
    res3 = shop.update(shopData,shopID,fileInfo)
    print(res3)

