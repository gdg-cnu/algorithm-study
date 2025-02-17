'''
주가가 비쌀 때 팔아야 하기 때문에
max 변수에 가장 큰 값을 저장
arr[i]이 max보다 작으면 차익으로 이득을 볼볼 수 있기 때문에
max에서 arr[i]를 빼주고 value(이익)에 더해준다.
'''

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    max=0
    value=0

    for i in range(len(arr)-1, -1, -1):
        if (arr[i]>max):
            max=arr[i]
        else:
            value+=max-arr[i]
    print(value)
