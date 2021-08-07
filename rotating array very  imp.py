def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

def rotate_right(arr,d,n):
    gcd=GCD(n,d)


    for i in range(gcd):

        j=i

        while 1:
            k=j+d
            if k>=n:
                k=k-n
            if k==i:
                arr[k]=tmp
                break
            tmp=arr[k]
            arr[k]=arr[j]
            arr[j]=tmp
            j=k
        print(arr)

arr=[1,2,3,4,5,6,7,8,9,10,11,12]
d=3
n=len(arr)
rotate_right(arr,d,n)
print(arr)
