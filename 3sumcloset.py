nums=list(map(int,input().split()))
target=int(input())
nums.sort()
closest=float('inf')

for i in range(len(nums)-2):
    left=i+1
    right=len(nums)-1

    while left<right:
        total=nums[i]+nums[left]+nums[right]

        if total==target:
          print(target)
          exit()
        if abs(total-target)<abs(closest-target):
           closest=total
        if total<target:
           left+=1
        else:
           right-=1

if closest!=float('inf'):
   print(closest)