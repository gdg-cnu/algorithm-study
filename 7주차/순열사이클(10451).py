# 순열 사이클
# dfs(v): 
# 노드 v 방문 표시 후 그 다음으로 갈 노드를 v를 통해 가져온다.
# 다음 노드 next가 아직 방문 전이라면 재귀를 통해 이동해준다다
def dfs(v):
    visited[v]=True
    next=s[v]
    if not visited[next]:
        dfs(next)

t=int(input())

for i in range(t):
    n=int(input())
    s= [0]+list(map(int, input().split()))
    visited=[False]*(n+1)
    count=0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
            count+=1
    print(count)


    




