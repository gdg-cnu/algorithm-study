
from collections import deque
import sys

input = sys.stdin.readline

n,m=map(int,input().split())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().strip())))


def bfs(x,y):
    q=deque([(x,y)])

    dx=[-1,1,0,0] 
    dy=[0,0,-1,1] 

    visited=[[False]*(m) for _ in range(n)] #방문여부 표시시

    dist = [[0]*m for _ in range(n)] #해당노드까지의 거리리
    
    dist[x][y]=1
    visited[x][y]=True
    
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if (0<=nx<n) and (0<=ny<m):
                if (not visited[nx][ny]) and (arr[nx][ny]==1):
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    dist[nx][ny]=dist[x][y]+1
            
                if  nx==n-1 and ny==m-1:
                    return dist[nx][ny]
    
    return -1

print(bfs(0,0))            