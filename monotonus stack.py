arr=[3,7,8,4]
stack=[]
for i in arr:
    while stack and stack[-1]>i:
        stack.pop()

    stack.append(i)

print(stack)
