import math
arr=list(map(int,input().split()))
h=int(input())

left=1
right=max(arr)

if not arr:
    print(0)
    exit()

while left<right:
    mid=(left+right)//2
    total=0
    for i in arr:
        total+=math.ceil(i/mid)
    if total>h:
        left=mid+1
    else:
        right=mid

print(left)