# 11501번

T = int(input())
for _ in range(T):
    # 날의 수 입력 받기
    N = int(input())
    # 주식 가격 리스트
    stock = list(map(int, input().split()))
    # 리스트 뒤집기
    stock.reverse()
    # 초기 최대 가격 설정
    max = stock[0]
    sum = 0

    #두번째 요소부터 탐색
    for i in range(1, N):
        # 더 높은 가격을 발견하면 갱신
        if max < stock[i]:
            max = stock[i]
            continue
        # 현재 가격이 max보다 작으면 이익 더하기기
        sum += max - stock[i]

    print(sum)  


