s=input()
n=len(s)
maxlen=0
maxstring=s[0]

for i in range(n-1):
    for j in range(i+1,n):
        if j-i+1 > maxlen and s[i:j+1]==s[i:j+1][::-1]:
            maxlen=j-i+1
            maxstring=s[i:j+1]

print(maxstring)