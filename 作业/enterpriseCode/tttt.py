str1='QCCSESSID=kt5dc60n6gir634tau0sgsjt12; zg_did=%7B%22did%22%3A%20%2217604420a9953b-093555f607ff9e-3e3e5f0e-1fa400-17604420a9a869%22%7D; UM_distinctid=17604420c575d3-0dc62e3a0e31ca-3e3e5f0e-1fa400-17604420c5832c; hasShow=1; _uab_collina=160638920645628606357947; CNZZDATA1254842228=230905684-1606387875-https%253A%252F%252Fwww.baidu.com%252F%7C1606405100; acw_tc=7250182516064092157255479efe8631bb1151a8622444a691cf347521; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201606409218984%2C%22updated%22%3A%201606409286032%2C%22info%22%3A%201606389205664%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%22efaf661dbcacb0a2e9b325ca773c75ba%22%7D'
str1=str1.replace(' ','')
list1=str1.split(';')
dict1={}
for ll in list1:
    ld=ll.split('=')
    dict1[ld[0]]=ld[1]
ls=[]
for one in dict1:
    tt={'value':dict1[one],'name':one}
    print(tt)
    print(type(tt))




