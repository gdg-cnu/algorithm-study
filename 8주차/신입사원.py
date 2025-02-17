# 1946번
# 서류 1등은 무조건 뽑히고 면접 등수를 비교하며 현재까지 선발된 사람중 면접 등수보다 낮으면 선발
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 지원자 수 입력
    N = int(input())
    # 서류, 면접 성적 저장하는 리스트
    rank = [list(map(int, input().split())) for _ in range(N)]
    # 서류 성적 기준 오름차순 정렬
    sort = sorted(rank)
    # 현재까지 면접 성적이 가장 좋은 사람의 인덱스(첫번째 요소를 기준으로 정렬)
    top = 0
    # 선발된 신입사원 수 (첫번째 사람은 무조건 선발)
    result = 1
    
    # 두번째 지원자부터 검사
    for i in range(1, len(sort)):
        # 현재 사람의 면접 등수가 기존 선발된 사람보다 성적이 더 좋다면
        if sort[i][1] < sort[top][1]:
            #top 값을 현재 지원자의 인덱스로 갱신
            top = i
            # 선발인원 +1 
            result += 1
    
    print(result)