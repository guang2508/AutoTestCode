import requests
from config import HOST
from lib.loginLib import Login
#1-定义一个类，叫课程管理
#2-子类课程管理继承父类Login
#3-(好处：子类的实例化对象能够调用父类的方法，能够访问父类的实例变量)
class CourseManage(Login):
    #1.新增课程
    def add(self,name,desc,display_idx):
        try:
            payload={
                'action':'add_course',
                'data':f'''{{
                  "name":"{name}",
                  "desc":"{desc}",
                  "display_idx":"{display_idx}"
                }}
                '''
            }
            #sessionid 需要通过cookie传给服务器，子类通过self调用父类的实例变量
            cookie={'sessionid':self.sessionID}
            #好的习惯是请求头按接口文档传
            header = {'Content-Type': 'application/x-www-form-urlencoded'}
            r=requests.post(f'{HOST}/api/mgr/sq_mgr/',data=payload,headers=header,cookies=cookie)
            return r.json()
        except:
            return {'retcode':'2','reason':'服务器错误'}

    #2.列出课程
    def list(self,pagenum,pagesize):
        payload={
            'action':'list_course',
            'pagenum':pagenum,
            'pagesize':pagesize
        }
        cookie = {'sessionid': self.sessionID}
        r=requests.get(f'{HOST}/api/mgr/sq_mgr/',params=payload,cookies=cookie)
        return r.json()

    #3.删除课程
    def delete(self,id):
        try:
            payload = {
                'action': 'delete_course',
                'id': id
            }
            cookie = {'sessionid': self.sessionID}
            header = {'Content-Type': 'application/x-www-form-urlencoded'}
            r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', data=payload,headers=header,cookies=cookie)
            # print(r.json())
            return r.json()
        except:
            return {'retcode': '2', 'reason': '服务器错误'}
    #4.修改课程
    def modify(self,id,name,desc,display_idx):
        payload = {
            'action': 'modify_course',
            'id': id,
            'newdata': f'''{{
                      "name":"{name}",
                      "desc":"{desc}",
                      "display_idx":"{display_idx}"
                    }}
                    '''
        }
        cookie = {'sessionid': self.sessionID}
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.put(f'{HOST}/api/mgr/sq_mgr/', data=payload,headers=header,cookies=cookie)
        return r.json()

    #5.新增课程2
    def add2(self,name,desc,display_idx):
        payload = f'''
                {{
                  "action" : "add_course_json",
                  "data"	 : {{
                    "name":"{name}",
                    "desc":"{desc}",
                    "display_idx":"{display_idx}"
                  }}
                }}
                '''
        header = {'Content-Type': 'application/json'}
        cookie = {'sessionid': self.sessionID}
        r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', data=payload.encode(),
                          cookies=cookie,headers=header)
        return r.json()


