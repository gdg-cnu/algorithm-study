import sys
input = sys.stdin.readline

n = int(input()) #사진틀개수
total = int(input()) #총추천횟수
students = list(map(int,input().split())) # 추천받은학생

photo=dict()

for i in range(len(students)):
  if students[i] in photo:
    photo[students[i]][0] += 1
  else:
    if len(photo) < n:
      photo[students[i]] = [1,i] 
    
    else:
      delList = sorted(photo.items(), key = lambda x : (x[1][0], x[1][1]))
      delKey = delList[0][0]
      del(photo[delKey])
      photo[students[i]] = [1, i]

ans_list = list(sorted(photo.keys()))
for ans in ans_list:
  print(ans,end=" ")


    



