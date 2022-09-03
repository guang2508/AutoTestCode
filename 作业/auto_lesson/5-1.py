import pprint
def putInfoToDict(fileName):
    checkinfo={}
    with open(fileName,'r+') as f1:
        infolist=f1.readlines()
        for i in infolist:
            info=i.strip().split('(')[1].split(')')[0]
            checkintime,lessonid,studentid=info.split(',')
            checkintime=checkintime.replace('\'','')
            lessonid=int(lessonid)
            studentid=int(studentid)
            lessoninfo={'lessonid': lessonid,'checkintime':checkintime}
            if studentid not in checkinfo:
                checkinfo[studentid]=[lessoninfo]
            else:
                checkinfo[studentid].append(lessoninfo)
    return checkinfo
pprint.pprint(putInfoToDict(r'C:\Users\Administrator\Desktop\签到.txt'))
