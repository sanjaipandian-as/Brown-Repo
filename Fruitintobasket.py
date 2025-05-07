from collections import Counter

fruits=list(map(int,input().split()))
basket=Counter()

left=0
maxlen=0

for right in range(len(fruits)):
    basket[fruits[right]]-=1
    while basket[fruits[left]]>2:
        basket[fruits[left]]-=1
        if basket[fruits[left]]==0:
            del basket[fruits[left]]

    maxlen=max(maxlen,right-left+1)

print(maxlen)