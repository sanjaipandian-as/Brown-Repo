def permutation(nums):
    res=[]
    def backtrack(p,r):
        if not r:
            res.append(p[:])
            return
        for i in range(len(r)):
            p.append(r[i])
            backtrack(p,r[:i]+r[i+1:])
            p.pop()
    backtrack([],nums)
    return res

nums=list(map(int,input().split()))
ress=permutation(nums)
print(ress)