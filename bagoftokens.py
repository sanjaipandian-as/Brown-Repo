a=list(map(int,input()))
power=int(input())
left=0
right=len(a)-1
maxscore=0
score=0

while left<=right:
    if power>=a[left]:
        power-=a[left]
        left+=1
        score+=1
        maxscore=max(maxscore,score)

    elif score>0:
        power+=a[right]
        right-=1
        score-=1
        maxscore=max(maxscore,score)

    else:
        break
print(maxscore)

a=list(map(int,input().split()))
left=0
right=len(a)-1
score=0
maxscore=0

for i in a:
    if power>=a[left]:
        power-=a[left]
        score+=1
        left+=1
        maxscore=max(maxscore,score)
    elif score>0:
        power+=a[right]
        score-=1
        right-=1
        maxscore=max(maxscore,score)

    else:
        break
print(maxscore)