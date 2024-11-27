import sys
n=int(sys.stdin.readline())
q=[]
h=0
t=0 
for i in range(n):
    commend=sys.stdin.readline().split()
    if commend[0]=='push':
        q.append(commend[1])
        h+=1

    elif commend[0]=='pop':
        if (h==t):
            print(-1)
        else:
            print(q[t])
            t+=1
            
    elif commend[0]=='size':
        print(h-t)
    elif commend[0]=='empty':
        if h==t:
            print(1)
        else:
            print(0)
    elif commend[0]=='front':
        if h==t:
            print(-1)
        else:
            print(q[t])
    elif commend[0]=='back':
        if h==t:
            print(-1)
        else:
            print(q[h-1])
