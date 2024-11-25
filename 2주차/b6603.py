def DFS(L, idx):
    if L==r:
        print(' '.join(map(str,result)))
    else:
        for i in range(idx,nums[0]):
                result[L]=nums[1+i]
                DFS(L+1, i+1)

if __name__=='__main__':
    while True:
        nums=list(map(int,input().split()))
        if nums[0]==0:
            break
        
        r=6
        result=[0]*r

        DFS(0,0)
        print()

