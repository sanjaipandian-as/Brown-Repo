

def backtrack(index,path):
    global maxlength
    if len(path)==len(set(path)):
        maxlength=max(maxlength,len(path))
    for i in range(index,len(arr)):
        backtrack(i+1,path+arr[i])
    return maxlength


arr=input()
maxlength=0
backtrack(0,"")

print(maxlength)