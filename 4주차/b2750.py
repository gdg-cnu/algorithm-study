n=int(input())
nums=[ int(input()) for _ in range(n)]

# 버블 정렬
for i in range(len(nums)-1,0,-1):
    for j in range(i):
        if nums[j]>nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for i in range(len(nums)):
    print(nums[i])