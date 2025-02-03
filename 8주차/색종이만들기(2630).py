import sys

input=sys.stdin.readline

n=int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,input().split())))

white=0
blue=0

def divide(r,c,n): #분할정복
    global white, blue #개수 저장
    fColor=paper[r][c] #첫번째 칸의 색
    
    for i in range(r,r+n):
            for j in range(c,c+n):
                if paper[i][j] != fColor:
                    divide(r,c,n//2)
                    divide(r,c+n//2,n//2)
                    divide(r+n//2,c,n//2)
                    divide(r+n//2,c+n//2,n//2)
                    return
    if fColor ==0:
        white += 1
    else:
        blue += 1
 

            
divide(0,0,n)
print(white)
print(blue)
                    


            
        
        

