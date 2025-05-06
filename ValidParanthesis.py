s=input()
stack=[]

for c in s:
    if c in ("(","{","["):
        stack.append(c)
    else:
        if not stack:
            print(False)
            exit()
        if c==")" and stack[-1]=="(" or c=="}" and stack[-1]=="{" or c=="]" and stack[-1]=="[":
            stack.pop()
        else:
            print(False)
            exit()
if not stack:
    print(True)
else:
    print(False)
