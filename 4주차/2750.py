
n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst_sorted=sorted(lst)

for i in lst_sorted:
    print(i)