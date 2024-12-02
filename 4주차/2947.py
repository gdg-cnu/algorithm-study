lst=list(map(int,input().split()))


while True:
    count=0
    for i in range(4):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
            count+=1
            for i in lst:
                print(i,end=" ")
            print()

    if count==0:
        break
