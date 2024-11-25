from collections import deque

n= int(input())

Que = deque(range(1, n+1)) 

while len(Que) > 1:  
    Que.popleft()  
    a = Que.popleft()  
    Que.append(a)  
    
print(Que[0]) 
    