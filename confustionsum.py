def confusion(char,s,k):
    

    count=0
    left=0
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

ans=max(confusion('T',s,k),confusion('F',s,k))
print(ans)


#  class Solution:
#     def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
#         def confussion(char):
#             count=0
#             left=0
#             maxlenth=0

#             for right in range(len(answerKey)):
#                 if answerKey[right]!=char:
#                     count+=1
#                 while count>k:
#                     if answerKey[left]!=char:
#                         count-=1
#                     left+=1
#                 maxlenth=max(maxlenth,right-left+1)
#             return maxlenth

#         max_f=confussion('F')
#         max_t=confussion('T')

#         return max(max_f,max_t)  Leet code solution
