#11497번

import sys

def solve():
    T = int(sys.stdin.readline().strip())  # 테스트 케이스 개수 입력

    for _ in range(T):
        n = int(sys.stdin.readline().strip())  # 통나무 개수 입력
        logs = list(map(int, sys.stdin.readline().split()))  # 통나무 높이 리스트 입력
        logs.sort()  #  통나무 높이를 오름차순 정렬

        # 정렬된 통나무를 최적의 순서로 배치할 리스트
        arranged = [0] * n
        left, right = 0, n - 1  # 왼쪽(left)과 오른쪽(right) 포인터 설정

        for i in range(n):
            if i % 2 == 0:
                arranged[left] = logs[i]  # 짝수 부분 왼쪽부터 채우기
                left += 1
            else:
                arranged[right] = logs[i]  # 오른쪽부터 채우기
                right -= 1

        # 인접한 통나무들의 높이 차이 중 최댓값 찾기
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(arranged[i] - arranged[(i + 1) % n]))  
            # (i + 1) % n:원형으로 이어진 통나무의 마지막과 첫 번째 비교 포함
            # 나머지 연산자를 이용해서 구함
        print(max_diff)  # 최댓값 출력

solve()
