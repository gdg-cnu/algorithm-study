nums=list(map(int,input().split()))
ans=[1,2,3,4,5]

while True:
    # 버블 정렬
    for i in range(0,4,1):
        if nums[i]>nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(" ".join(map(str,nums)))

    if nums==ans:
        break