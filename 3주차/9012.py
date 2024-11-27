#괄호
import sys
t=int(sys.stdin.readline())

for i in range(t):
    ps = list(sys.stdin.readline().strip())
    stack=[]
    vps=True
    for j in range(len(ps)):
        if ps[j]=='(':
            stack.append('(')
        else:
            if len(stack)==0:
                vps=False
                break
            else:
                stack.pop()
            
    if (vps==True) and (len(stack)==0):
        print("YES")
    else:
        print("NO")
