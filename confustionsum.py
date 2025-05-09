def confusionexam(char,s,k):
    left=0
    count=0
    maxlength=0

    for right in range(len(s)):
        if s[right]!=char:
            count+=1
        while count>k:
            if s[left]!=char:
                count-=1
            left+=1

        maxlength=max(maxlength,right-left+1)

    return maxlength        


s=input()
k=int(input())

res=max(confusionexam("F",s,k),confusionexam("T",s,k))
print(res)