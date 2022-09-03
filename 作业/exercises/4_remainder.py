# def remainder(num1,num2):
#     return num1%num2
# num1=input('输入第一个数字：')
# num2=input('输入第二个数字：')
# print(int(remainder(float(num1),float(num2))))

def remainde(aa,bb):
    if aa.isdigit==True and bb.isdigit==True:
        return float(aa)%float(bb)
    else:
        return "输入的数据有误"
s1=input("1")
s2=input("2")
print(remainde(s1,s2))