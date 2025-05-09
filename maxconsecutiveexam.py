stones=list(map(int,input().split()))
stones.sort()
n=len(stones)
left=0
max_moves=max(stones[-1]-stones[1]-n+2,stones[-2]-stones[0]-n+2)
min_move=n

for right in range(len(stones)):
    while stones[right]-stones[left]+1>n:
        left+=1
    current_window=right-left+1
    if current_window==n-1 and stones[right]-stones[left]==n-2:
        min_move=min(min_move,2)
    else:
        min_move=min(min_move,n-current_window)

print(min_move,max_moves)