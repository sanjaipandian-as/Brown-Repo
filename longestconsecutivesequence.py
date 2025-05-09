nums=list(map(int,input().split()))
nums.sort()
numset=set(nums)
longest=0

for num in nums:
    if num-1 not in numset:
        length=1
    while num+length in numset:
        length+=1
    longest=max(longest,length)

print(longest)