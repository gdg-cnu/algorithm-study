'''
신맛 - 사용한 재료의 신맛의 곲
쓴맛 - 합
목표: 신맛과 쓴맛의 차이 최소
'''
from itertools import combinations #완전탐색을 위한 조합 사용

n=int(input())
res=float('inf') #무한대로 초기화 - 가장 큰 값이 되도록록
nums=[list(map(int,input().split())) for _ in range(n)]

for i in range(1,n+1):
    for num in combinations(nums,i):
        sour=1
        bitter=0

        for s, b in num:
            sour*=s
            bitter+=b

        res=min(res, abs(sour-bitter))

print(res)