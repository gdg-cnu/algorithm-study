from sys import stdin
from collections import deque

n = int(stdin.readline())  # 명령어의 개수
Que = deque([])  # 빈 덱 초기화

for i in range(n):
    order = stdin.readline().split()  # 명령어 입력

    if order[0] == 'push': 
        Que.append(order[1])  # 큐에 값 추가

    elif order[0] == 'pop': 
        if len(Que) == 0:
            print(-1)  # 큐가 비었으면 -1 출력
        else:
            print(Que.popleft())  # 큐의 첫 번째 값 제거 및 출력

    elif order[0] == 'size': 
        print(len(Que))  # 큐의 크기 출력

    elif order[0] == 'empty':
        if len(Que) == 0:
            print(1)  # 큐가 비었으면 1 출력
        else:
            print(0)  # 아니면 0 출력

    elif order[0] == 'front':
        if len(Que) == 0:
            print(-1)  # 큐가 비었으면 -1 출력
        else:
            print(Que[0])  # 큐의 첫 번째 값 출력

    elif order[0] == 'back':
        if len(Que) == 0:
            print(-1)  # 큐가 비었으면 -1 출력
        else:
            print(Que[-1])  # 큐의 마지막 값 출력
