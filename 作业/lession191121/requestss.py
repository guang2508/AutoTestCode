import requests
# r=requests.get('http://www.baidu.com')
# print(r.text)

# payload={"action":"list_course","pagenum":"1","pagesize":"20"}
# r=requests.get('http://localhost:81/api/mgr/sq_mgr/',params=payload)
# print(r.text)

# payload={"action":"add_course",
#          "data":'''{"name": "初中化学",
# 	"desc": "初中化学课程",
# 	"display_idx": "4"
#             }'''
#             }
# headers={"Content-Type":"application/x-www-form-urlencoded"}
# r=requests.post('http://localhost:81/api/mgr/sq_mgr/',headers=headers,data=payload)
# print(r.text)

# payload={
#   "action" : "add_course_json",
#   "data"	 : {
#     "name":"初中111化1学",
#     "desc":"初中化学课程",
#     "display_idx":"4"
#   }
# }
# import json
# header={"Content-Type":"application/json"}
# r=requests.post('http://localhost:81/apijson/mgr/sq_mgr/',headers=header,json=payload)
# print(r.text)

