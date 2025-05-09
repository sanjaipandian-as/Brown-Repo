nums=list(map(int,input().split()))
nums.sort()
i=0
j=0
n=len(nums)

while j<n:
    if nums[i]<nums[j]:
        i+=1
    j+=1

print(i)