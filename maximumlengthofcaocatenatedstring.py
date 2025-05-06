arr=input().split()

max_lenght=0
def backtrack(index,path):
    global max_lenght
    if len(path)==len(set(path)):
        max_lenght=max(max_lenght,len(path))
    for i in range(index,len(arr)):
        backtrack(i+1,path+arr[i])
    

backtrack(0,"")
  
print(max_lenght)