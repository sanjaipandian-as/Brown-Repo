arr=list(map(int,input().split()))
k=int(input())

count=0
left=0
right=len(arr)-1

while left<right:
    if arr[right]+arr[left]==k:
        count+=1
        left+=1
        right-=1

    elif arr[right]+arr[left]<k:
        left+=1
    elif arr[right]+arr[left]>k:
        right-=1

print(count)