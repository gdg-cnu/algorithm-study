import sys
input = sys.stdin.readline
n=int(input())
video=[list(map(int,input().strip())) for _ in range(n)]

def quadTree(r,c,n): #분할정복복

    fNum=video[r][c] # 첫번째 칸의 수

    for i in range(r,r+n):
        for j in range(c,c+n):
            if fNum != video[i][j]:
                print("(",end="")
                quadTree(r,c,n//2)
                quadTree(r,c+n//2,n//2)
                quadTree(r+n//2,c,n//2)
                quadTree(r+n//2,c+n//2,n//2)
                print(")", end="")
                return

    if fNum == 0:
        print(0,end="")
    else:
        print(1,end="")

quadTree(0,0,n)