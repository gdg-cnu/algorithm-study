import sys
input = sys.stdin.readline

n,m = map(int,input().split())

if n==1:
  count=1
elif n==2:
  if m<=6:
    count = 1 + (m-1)//2
  else:
    count=4
else: #m<=3
  if m<5:
    count=m
  elif m==5 or m==6:
    count=4
  else:
    count=m-2

print(count)





        
        

    