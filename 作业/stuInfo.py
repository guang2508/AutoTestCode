def stuInfomation(stu):             #输入学生信息，按规格打印学生信息
    stuList=stuInfo.split(';')      #各个学生信息进行分割
    for one in range(0,len(stuList)-1,1):   #循环次数，去掉最后一个学生信息的分号所占次数
        stu=stuList[one]
        name=(stu.split(',')[0]).replace(' ','')    #先分割，后替换空格
        age=(stu.split(',')[1]).replace(' ','')
        print(f'{name:<20}:{age:>02};')


stuInfo = 'Jack Green ,   21  ;  Mike Mos, 9;'  # 学生信息，为调试方便就不用input了
stuIn=stuInfomation(stuInfo)        #调用函数


#
