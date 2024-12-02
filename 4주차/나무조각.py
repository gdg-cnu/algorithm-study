# 2947번

s=list(map(int,input().split()))

while 1:
    for i in range(4):
        if s[i]>s[i+1]:
            s[i], s[i+1] = s[i+1], s[i]
            print(" ".join(map(str,s)))
    if s == [1, 2, 3, 4, 5]: 
        break


