arr=list(map(int,input().split()))
k=int(input())

left=0
for right in range(len(arr)):
    if arr[right]==0:
        k-=1
    if k<0:
        if arr[left]==0:
            k+=1
        left+=1

print (right-left+1)