import sys
n=int(sys.stdin.readline())
lst=[]
for _ in range(n):
    a, b = sys.stdin.readline().split()
    lst.append([int(a), b])

lst.sort(key=lambda x:x[0])

for a, b in lst:
    print(a,b)