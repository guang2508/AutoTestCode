import requests
import hashlib

userName="ma0342"
psw="55382"
def get_md5(psw):
    m = hashlib.md5()
    m.update(psw.encode("utf-8"))  #55382密码进行MD5加密
    return m.hexdigest()    #返回16进制
ip='121.41.14.39:8082'
payload={"username":userName,"password":get_md5(psw)}
header={"Accept":"application/json"}
r=requests.post(f'http://{ip}/account/sLogin',data=payload,headers=header)
print(r.text)





