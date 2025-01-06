# 10814번

N=int(input())
person=[]

for i in range(N):
    age,name= input().split()
    person.append((int(age),name)) # 튜플로 추가

person.sort(key= lambda x:x[0]) # 나이 기준 정렬

for i in range(len(person)):
    print(person[i][0],person[i][1])

