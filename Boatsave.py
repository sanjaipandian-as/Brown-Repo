arr=list(map(int,input().split()))
limit=int(input())
boat=0
arr.sort()

left=0
right=len(arr)-1

while left<=right:
    if arr[left]+arr[right]<=limit:
        left+=1
    right-=1
    boat+=1

print(boat)

