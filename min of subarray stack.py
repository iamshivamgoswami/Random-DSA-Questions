arr= [71,55,82,55]
left=[]
stack=[]
for ind,i in enumerate(arr):
    if not stack:
        left.append(-1)
    elif stack and arr[stack[-1]]<=i:
        left.append(stack[-1])
    elif stack and arr[stack[-1]]>=i:
        while stack and arr[stack[-1]]>i:
            stack.pop()
        if stack:
            left.append(stack[-1])
        else:
            left.append(-1)

    stack.append(ind)
print(left)
for i in range(len(left)):
    left[i]=i+1 if left[i]==-1 else i-left[i]
print(left)
right=[]
stack=[]
for i in range(len(arr)-1,-1,-1):
    if not stack:
        right.append(-1)
    if stack and arr[stack[-1]]<=arr[i]:
        right.append(stack[-1])
    elif stack and arr[stack[-1]]>arr[i]:
        while stack and arr[stack[-1]]>arr[i]:

            stack.pop()
        if not stack:
            right.append(-1)
        else:
            right.append(stack[-1])


    stack.append(i)
right.reverse()
for i in range(len(right)):
    right[i]=len(right)-i if right[i]==-1 else right[i]-i


print(right)
ans=0
for i,j,k in zip(arr,left,right):
    ans+=i*j*k
print(ans)



