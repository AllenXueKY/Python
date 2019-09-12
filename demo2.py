import time
from math import sqrt
start = time.time()
result = []
def prime(n):
    flag = [1]*(n+2)
    p=2
    text=[]
    while(p<=n):
        text.append(p)
        for i in range(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break
    return text
def isprime(n):
    if n==2 or n==3:
        return 1
    if n%6!=1 and n%6!=5:
        return 0
    tmp =int(sqrt(n))
    for i in range(5,tmp+1,6):
        if (n%i== 0 or n%(i+2)==0):
            return 0
    return 1
for i in prime(1000000):
#         if((i in prime(1000000)) and  (i+2 in prime(i+2))):
     if isprime(i) and isprime(i + 2):
        result.append((i, i + 2))
with open("result.txt", "w") as f:
    for i, j in result:
        f.write("%d,%d\n" % (i, j))
end = time.time()
print("脚本运行时间:%.4f秒，一共找到%d组结果。" % (end - start, len(result)))