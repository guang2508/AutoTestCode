file_salary='G:\\软件测试\\作业\\file1.txt'
fo=open(file_salary)
lines=len(fo.readlines())
fo.seek(0)
for one in range(0,lines):
    payroll=fo.readline()
    temp=payroll.split(';')
    name=temp[0].split(':')[1].strip()
    salary=temp[1].split(':')[1].strip()
    tax=round(int(salary)*0.1)
    afterTax=round(int(salary)*0.9)
    file_salary2='G:\\软件测试\\作业\\file2.txt'
    f2=open(file_salary2,'a')
    file_salary2=f2.write(f'name: {name:<7};    salary:{salary:>7} ;  tax:{tax:>5} ; income:{afterTax:>7}\n')



