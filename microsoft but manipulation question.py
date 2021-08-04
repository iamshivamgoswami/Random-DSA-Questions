import time

s="011100"
start=time.time()
a=int(s,2)

count=0
while a>1:
    if a&1==0:
        a=a>>1
        count+=1

    else:
        a=a>>1
        count+=2
print(a)
print(count+1)
print(time.time()-start)

