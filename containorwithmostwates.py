arr=list(map(int,input().split()))
left=0
right=len(arr)-1
maxarea=0
while left<right:
    widht=right-left
    area=widht*min(arr[left],arr[right])
    maxarea=max(maxarea,area)

    if arr[left]<arr[right]:
        left+=1
    else:
        right-=1

print(maxarea)