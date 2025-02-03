import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

lst.sort()

min_indx=0
max_indx=n-1
s= lst[min_indx]+lst[max_indx]
answer=(lst[min_indx],lst[max_indx])

while min_indx < max_indx:

    result=lst[min_indx]+lst[max_indx]
    if abs(result) < abs(s):
        s=result
        answer=(lst[min_indx],lst[max_indx])
    
    if result==0:
        break
    elif result>0:
        max_indx-=1 
    else:
        min_indx+=1
    
    
print(answer[0], answer[1])




