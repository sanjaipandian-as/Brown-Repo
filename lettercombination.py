def lettercombination(digit):
    res=[]
    digit=str(digit)
    if not digit:
        return[]
    
    hash_map={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

    def backtrack(index,path):
        if index==len(digit):
            res.append("".join(path))
            return
        for letter in hash_map[digit[index]]:
            path.append(letter)
            backtrack(index+1,path)
            path.pop()
    backtrack(0,[])
    return res

digit=int(input())
print(lettercombination(digit))
