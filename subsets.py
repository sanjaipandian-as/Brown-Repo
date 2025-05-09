nums=list(map(int,input().split()))
maxsum=float('-inf')

cursum=0

for num in nums:
    cursum=num
    maxsum=max(maxsum,cursum)

    if cursum<0:
        cursum=0

print(maxsum)