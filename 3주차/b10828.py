import sys

n = int(input())
stack=[]

for i in range(n):
    s = sys.stdin.readline().rstrip()
    if s.startswith('push'):
        stack.append(int(s.split()[1]))
    elif s=='top':
        if stack:
            print(stack[-1])
        else: print(-1)
    elif s=='size':
        print(len(stack))
    elif s=='empty':
        if stack:
            print(0)
        else:
            print(1)
    elif s=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)