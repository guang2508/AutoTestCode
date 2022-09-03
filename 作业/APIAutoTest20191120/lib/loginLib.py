import requests
from config import HOST
class Login:
    #用户登录
    def login(self,username,password):
        payload={"username":f"{username}",
                 "password":f"{password}"
                 }
        r=requests.post(f'{HOST}/api/mgr/loginReq',data=payload)
        # print(r.json())
        # print(r.cookies['sessionid'])
        #定义一个实例变量（属性），叫：sessionID，子类可以通过self调用
        self.sessionID=r.cookies['sessionid']
        return r.json(),r.cookies['sessionid']
