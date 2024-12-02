# 1427번

n= str(input())

list=[]

for i in n:
    list.append(i)

list.sort(reverse=True)

for i in list:
    print(i, end="")

