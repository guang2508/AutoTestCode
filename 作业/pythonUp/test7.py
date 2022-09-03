# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-04
import os,sys
import time
import shutil
sourcefile='G:\\apk\\ffmpeg-20191203-12bbfc4-win64-static\\bin\\'
def record():   #录制
    global sourcefile
    now = time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))    #当前时间格式：20170329_202814
    fname=now+r".mp4"   #录制产生的文件名
    rcommend=f'ffmpeg.exe -y -rtbufsize 100M -f gdigrab -framerate 10 -draw_mouse 1 -i desktop -c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M "{fname}"'
    os.system(f'''g: &&cd {sourcefile} &&{rcommend}''')  #录制

# def combine():  #合并
#     ccommend=f'ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4'
#     os.system(f'''g: &&cd {sourcefile} &&{ccommend}''')
# 列出指定文件夹指定格式的文件,并排序，返回带排序字典,参数：路径，文件类型
def SFileToDFile(sourcefile, fileclass,filelist):
    # 遍历目录和子目录
    for filenames in os.listdir(sourcefile):
        # 取得文件或文件名的绝对路径
        filepath = os.path.join(sourcefile, filenames)
        # 判断是否为文件夹
        if os.path.isdir(filepath):
            # 如果是文件夹，重新调用该函数
            SFileToDFile(filepath, fileclass)
        # 判断是否为文件
        elif os.path.isfile(filepath):
            # 如果该文件的后缀为用户指定的格式，则列出
            filepath=os.path.basename(filepath)
            if filepath.endswith(fileclass):
                filelist.append(filepath)
    newlist = sorted(filelist, key=lambda i: i[0],reverse=False)
    num=1
    filedicts={}
    for list in newlist:
        filedicts[num]=list
        num+=1
    return filedicts

# def
filelist=[]
se=input('选择您要做的操作：1：录制视频，2：合并视频:')
if se=='1':
    print("输入 q 结束录制")
    record()

elif se=='2':
    fileDicts=SFileToDFile(sourcefile,'.mp4',filelist)
    # print(type(fileDicts))
    for fileDict in fileDicts:
        # print(fileDict)
        print(f'{fileDict} - {fileDicts[fileDict]}')
    str=input('请输入要合并视屏的文件号（格式1，2，3，4）：')   #假设输入正确，不作判断了
    comLists=list(eval(str))
    with open(f'{sourcefile}concat.txt', 'w+') as comList:
        for i in comLists:
            comList.write('file '+fileDicts[i]+'\n')
        # re=comList.read()
    ccommend = f'ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4'
    os.system(f'''g: &&cd {sourcefile} &&{ccommend}''')
else:
    print('你的输入不正确')









