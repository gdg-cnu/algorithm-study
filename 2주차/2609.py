


a,b=map(int,input().split())
list=[]
for i in range(1,min(a,b)+1):
    if a%i ==0 and b%i ==0:
        list.append(i)

print(max(list))
print(max(list)*(a//max(list))*(b//max(list)))
