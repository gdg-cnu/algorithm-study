# 5014번
# 1. queue 생성, s추가하기
# 2. visited 리스트 생성
# 3. queue에서 값 빼주기
# 4. 만약 목표층에 도달하면 visited[x] 반환
# 5. x+u, x+d층 반복하면서 안 간 층이면 i를 queue에 추가하고 새로운 층에 올 때마다 이전층의 방문횟수 1 더하기

from collections import deque

f, s, g, u, d = map(int, input().split())

def BFS():
    queue = deque()
    queue.append(s)
    visited = [0] * (f + 1)

    while queue:
        x = queue.popleft()

        if x == g:  # 목표 층 도달
            return visited[x]  # 버튼 누른 횟수 반환
        
        for i in (x + u, x - d):  
            if i == x:  # 이동하지 않는 경우 제외 (u=0 또는 d=0)
                continue
            if 1 <= i <= f:  # 유효한 층 범위 내
                if visited[i] == 0:  # 아직 방문하지 않은 층
                    queue.append(i)
                    visited[i] = visited[x] + 1  # 방문 횟수 갱신

    return "use the stairs"

# 결과 출력
print(BFS())
