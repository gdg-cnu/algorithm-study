# 2961번

from itertools import combinations

N=int(input()) # 재료의 개수 입력
materials=[list(map(int,input().split())) for _ in range(N)] # 재료의 신맛, 쓴맛 이중 리스트
result=1e9 # 10억으로 초기화

# i를 1부터 n까지 증가시키면서 i개의 원소를 선택하는 조합 만들기
for cmbs in [combinations(materials,i) for i in range(1,N+1)]:
    for c in cmbs:
        S,B=1,0       # 신맛, 쓴맛 초기화
        for s,b in c: # 각 조합에 대해
            S*=s;B+=b # 신맛은 곱하고, 쓴맛은 더한다
        result=min(result, abs(S-B)) # s-b값이 현재 최소값보다 작다면 갱신

print(result)