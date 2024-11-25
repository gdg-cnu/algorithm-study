from sys import stdin

n = int(stdin.readline())
Que = []

for i in range(n) :
    order = stdin.readline().split()
    if order[0] == 'push' : 
        Que.append(order[1])

    elif order[0] == 'pop' : 
        if len(Que) == 0:
            print(-1)
        else:
            print(Que.pop(0))

    elif order[0] == 'size' : 
        print(len(Que))

    elif order[0] == 'empty' :
        if len(Que) == 0 : 
            print(1)
        else : 
            print(0)
            
    elif order[0] == 'front':
        if len(Que) == 0 : 
            print(-1)
        else : 
            print(Que[0])
    
    elif order[0] == 'back' :
        if len(Que) == 0 : 
            print(-1)
        else : 
            print(Que[-1])