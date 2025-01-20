from collections import deque
import sys
input=sys.stdin.readline

m,n=map(int,input().split())
arr=[]
for i in range(n):
        arr.append(list(map(int,input().split())))

day=0

dx=[0,0,-1,1]
dy=[-1,1,0,0]
    
q=deque([])

def bfs():

    for i in range(n):
          for j in range(m):
                if arr[i][j]==1:
                      q.append((i,j))
 
    while q:
          x,y=q.popleft()
          for i in range(4):
                nx= x+dx[i]
                ny= y+dy[i]
                if (0<=nx<n) and (0<=ny<m):
                      if arr[nx][ny]==0:
                            arr[nx][ny]=arr[x][y]+1
                            q.append((nx,ny))
                                     
    day=0
    for i in arr:
        for j in i:
            if j==0:
                return -1
        day=max(day,max(i))
    
    return day-1    
  
        
          
print(bfs())          
    
            
                                    
        


