#연결요소 개수 구하기
# N, M=input *sys.stdin.readline 이용해야 시간초과X
# 초기값을 0으로하는 그래프의 인접행렬 g 선언
# 정점 a,b 입력 후 g의 해당 위치에 1 넣기기
# 방문리스트 생성성
# dfs(v) *스택,재귀 이용
# 방문처리 # 방문 후 정점 출력
# 방문기록에 없고, 인덱스에 값이 있다면 방문한다. 재귀 함수 활용
#
# dfs 함수 생성 후 for문을 이용하여 visted[i]==False인 노드가 없어질 때까지 dfs 수행
# 수행 시마다 count 1씩 증가
# 
# **sys.setrecursionlimit(재귀호출의 깊이 한도를 설정하는 함수수) 지정해줘야 런타임 에러 발생x
# 
import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n,m = map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    g[a][b]=1
    g[b][a]=1

visited=[False]*(n+1)

def dfs(v):
    visited[v]=True
    for i in range(1,n+1):
        if not visited[i] and g[v][i]==1:
            dfs(i)

count =0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count+=1
dfs(1)
print(count)