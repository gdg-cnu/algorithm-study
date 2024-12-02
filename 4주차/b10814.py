n=int(input())
arr=[]

for _ in range(n):
    x, y = input().split()
    arr.append([int(x),y])

arr.sort(key=lambda user:int(user[0]))
for i in range(0,n):
    print(arr[i][0], arr[i][1])