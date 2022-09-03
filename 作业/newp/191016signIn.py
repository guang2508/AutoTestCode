signinDict={}

lessonList=[]

def putInfoToDict(fileName):
    lines=fileName.read().splitlines()
    for one in lines:
        temp=one.split(',')
        checkintime=temp[0][1:]
        if '(' in checkintime:
            checkintime=checkintime.split('(')[1]
        lessonid=temp[1]
        studentid=int(temp[2][:-1])
        if studentid not in signinDict:
            lessonDict = {}
            lessonDict['lessonid']=lessonid
            lessonDict['checkintime']=checkintime
            lessonList=lessonDict
            signinDict[studentid]=lessonList

        else:
            lessonDict = {}
            lessonDict['lessonid'] = lessonid
            lessonDict['checkintime'] = checkintime
            lessonList=signinDict[studentid].values

            lessonList.append(lessonDict)
    return signinDict
signIN='G:\\软件测试\\作业\\0005_1.txt'
with open(signIN) as fo:
    putInfoToDict(fo)
    print(signinDict)

