tokens=list(map(int,input().split()))
power=int(input())

left=0
right=len(tokens)-1
score=0
maxscore=0

while left<=right:
    if power>=tokens[left]:
        power-=power[left]
        left+=1
        score+=1
        maxscore=max(maxscore,score)
    elif score>0:
        power+=tokens[right]
        right-=1
        score-=1
        maxscore=max(maxscore,score)
    else:
        break
print(maxscore)
