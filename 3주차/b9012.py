import sys

n=int(input())
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    stk=[]

    for i in s:
        if i=='(':
            stk.append('(')
        elif i==')':
            if stk:
                stk.pop()
            else:
                stk.append(')')
                break

    if stk:
        print("NO")
    else:
        print("YES")
