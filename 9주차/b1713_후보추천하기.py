n=int(input())
m=int(input())
votes=list(map(int,input().split())) # 추천받은 학생 목록

#딕셔너리로 해서 들어오는 순서대로 넣기
res={}

for i in votes:
    if i in res:
        res[i]+=1
    else:
        if len(res)>=n: # 후보자가 틀보다 많은 경우
            #res[x](추천횟수)을 기준으로 x(추천학생)찾아냄
            min_value=min(res,key=lambda x:(res[x])) 
            res.pop(min_value)
        res[i]=1 #새로운 학생 제거

print(*sorted(res.keys()))
