a, b = map(int, input().split())
ab=a-b

for i in range(a-1,1,-1):
    a*=i

for i in range(b-1,1,-1):
    b*=i

for i in range(ab-1,1,-1):
    ab*=i

print(a//(b*ab))
