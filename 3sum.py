nums=list(map(int,input().split()))
nums.sort()
res=[]
target=0

n=len(nums)
for i in range(n-2):
    if i>0 and nums[i]==nums[i-1]:
        continue
    left=i+1
    right=n-1

    while left<right:
        total=nums[i]+nums[left]+nums[right]
        if total==target:
            res.append([nums[i],nums[right],nums[left]]) 
            while left<right and nums[left]==nums[left+1]:
                left+=1
            while left<right and nums[right]==nums[right-1]:
                right-=1
            
            left+=1
            right-=1

        elif target<0:
            left+=1
        else:
            right-=1

print(*res)