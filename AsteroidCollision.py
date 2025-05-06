a=list(map(int,input().split()))
stack=[]

for stone in a:
    while stack and stone<0 and stack[-1]>0:
        if abs(stone)>abs(stack[-1]):
            stack.pop()
        elif abs(stone)==abs(stack[-1]):
            stack.pop()
            break
        else:
            break
    else:
        stack.append(stone)
print(stack)

arr=list(map(int,input().split()))
stack=[]

for stone in arr:
    while stack and stone<0 and stack[-1]>0:
        if abs(stone)>abs(stack[-1]):
            stack.pop()
        elif abs(stone)==abs(stack[-1]):
            stack.pop()
            break
        else:
            break
print(stack)
# boat is the only way to go in sea there is no other way go thourgh sea