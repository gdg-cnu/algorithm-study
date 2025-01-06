# 문제 정의
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하기

# 의사 코드
# 함수 func(n):
#    dp 배열 생성
#    dp[1] =1 초기값 설정
#    만약 n이 1보다 크면 
#       dp[2]=2 값 설정
#    만약 n이 2보다 크면 
#       dp[3]=4 값 설정
#    4부터 n+1까지 반복하며
#         dp[i]=dp[i-1]+ dp[i-2]+dp[i-3]
#     dp[n] 반환

def func(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    if n > 2:
        dp[3] = 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

T = int(input())
for i in range(T):
    n = int(input())
    print(func(n))