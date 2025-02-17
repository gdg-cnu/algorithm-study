import sys
input = sys.stdin.readline

t=int(input())

for i in range(t):
  grade=[]
  n=int(input())
  for i in range(n):
    grade.append(list(map(int,input().split())))
  
  grade.sort() #서류 점수 기준으로 정렬렬
  check = grade[0][1]
  count=1 

  for i in range(1,n):
    if grade[i][1] < check: #면접 등수수가 앞사람보다 높으면 합격
      check = grade[i][1]
      count+=1
  print(count)

  