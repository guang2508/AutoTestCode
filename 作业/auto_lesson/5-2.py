def salaryinfo(filename):
    with open(filename,'r+') as f1,open(r'C:\Users\Administrator\Desktop\file2.txt','w+') as f2:
        salarylist=f1.readlines()
        for i in salarylist:
            name_info=i.replace(' ','').split(';')[0].split(':')[1]
            salary_info=int(i.replace(' ','').split(';')[1].split(':')[1].replace('\n',''))
            tax_info=int(salary_info*0.1)
            income_info=int(salary_info*0.9)
            f2.write(f'name:{name_info:<7} ;    salary:{salary_info:>7} ; tax:{tax_info:>6} ;income:{income_info:>7}\n')
filename=r'C:\Users\Administrator\Desktop\file1.txt'
salaryinfo(filename)