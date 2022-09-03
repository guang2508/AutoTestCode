with open('./乘法表.txt','w+') as cfb:
    for i in range(1,10):
        for j in range(1,i+1):
            cfb.write(f'{j}*{i}={i*j}\t')
        cfb.write('\n')