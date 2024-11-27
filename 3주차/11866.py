n ,k = map(int, input().split())

lst=[i for i in range(1, n+1)]
ysfs=[]
k=k-1
index=k
while len(ysfs)<n:
    if (index)>=len(lst):
        index-=len(lst)
    else:
        ysfs.append(str(lst.pop(index)))
        index+=k
    

print('<'+', '.join(ysfs)+'>')
