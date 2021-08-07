def GCD(a,b):
    if b==0:
        return a
    return (b,a%b)
def left_rotate(arr,d,n):
    d=d%n
    gcd=GCD(d,n)
    for i in range(len(gcd)):
        j=i
        tmp=arr[i]
        while 1:
            k=j+d
            if k>=n:
                k=k-n
            if k==i:
                break
            arr[j]=arr[k]
            j=k
        arr[j]=tmp

arr=[1,2,3,4,5,6,7,8,9,10,11,12]
left_rotate(arr,3,len(arr))
print(arr)