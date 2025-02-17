'''
서류심사 성적, 면접 성적을 rank 배열에 입력
rank배열을 정렬 -> 0번에 오는 사람은 무조건 합격임
-> 하나라도 다른사람들보다 높기 때문에!
면접 성적으로 비교를 해야함.
서류심사 1등의 면접 순위와 비교해서
더 낮으면 cnt를 1더해줌
'''
import sys

t=int(input())
for _ in range(t):
    n=int(input())
    rank=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    rank.sort()
    
    cnt=1
    max=rank[0][1]
    for i in range(1,n):
        if max > rank[i][1]:
            cnt+=1
            max=rank[i][1]

    print(cnt)


