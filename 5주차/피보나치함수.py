# 문제 정의
# 피보나치 수열에서 원하는 수를 호출 했을 때, 0과 1이 총 몇번 호출되는지 세기

# 의사 코드
# 입력 T받기
# T번 반복:
#     입력 N받기
#     a,b=1,0 초기값 설정
#     N번 반복:
#         a=b 
#         b=a+b
#     a,b  출력하기

T=int(input())
for i in range(T):
    N=int(input())
    a,b=1,0
    for i in range(N):
        a,b=b,a+b
    print(a,b)