'''
높이차가 최소가 되어야함
난이도는 인접한 두 통나무 간의 높이차의 최대값
원형이기 때문에 단순 정렬시 첫 값과 끝 값의 차가 높게나옴
가장 최적은 작은 값과 큰 값을 번갈아가면서 배치한 것
'''
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    arr=sorted(list(map(int,input().split())))
    level=0
    for i in range(2,n):
        level=max(level,abs(arr[i]-arr[i-2]))
    print(level)