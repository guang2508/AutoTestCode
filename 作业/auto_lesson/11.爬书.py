import re
import requests
req=requests.get('http://www.china-audit.com/lhd_0zftl8lxn168ub00wpi6_1.html')
# print(req.text)
mulu=re.findall('html" title="(第.*?)" target="_blank">',req.text)
# for i in range(12,len(mulu)):
for i in range(12,17):
    wangzhiID=re.findall(f'/d/1020/(.*?).html" title="{mulu[i]}" target="_blank">',req.text)[0]
    # print(wangzhiID,mulu[i])
    # print('https://www.qzguermei.com/d/1020/'+wangzhiID,mulu[i])
    req1 = requests.get(f'https://www.qzguermei.com/d/1020/{wangzhiID}.html')
    # print(req1.text)
    neirong=re.findall('<div class="content" id="chaptercontent">(.*?)<br/><br/>全书网手机阅读地址https://m.qzguermei.com',req1.text,re.S)[0]
    # print(neirong)
    neirong=neirong.split('<br/><br/>　　')
    # print(neirong)

        # print(i)
    with open(f'./{mulu[i]}.txt','w+') as f1:
        for i in neirong:
            f1.write(i+"\n")
