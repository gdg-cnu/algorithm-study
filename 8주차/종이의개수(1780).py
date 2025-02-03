import sys

input=sys.stdin.readline

n = int(input())
paper=[]
for i in range(n):
    paper.append(list(map(int,input().split())))
arr=[0,0,0] #-1,0,1 개수 저장장

def divide(r,c,n):
    global arr
    fNum=paper[r][c]

    for i in range(r,r+n):
        for j in range(c,c+n):
            if fNum != paper[i][j]:
                n//=3
                divide(r,c,n)
                divide(r,c+n,n)
                divide(r,c+ 2*n ,n)
                divide(r+n,c,n)
                divide(r+n,c+n,n)
                divide(r+n, c+2*n ,n)
                divide(r+2*n,c,n)
                divide(r+2*n,c+n,n)
                divide(r+2*n,c+2*n ,n)
                return
    if fNum == -1:
        arr[0] += 1
    elif fNum == 0:
        arr[1] += 1
    else:
        arr[2] += 1

    
    
divide(0,0,n)

print(arr[0]); print(arr[1]); print(arr[2])



            
