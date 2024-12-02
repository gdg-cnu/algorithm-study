n=input()
lst=list(n)
intlst=list(map(int,lst))

intlst.sort(reverse=True)
for i in intlst:
    print(i,end="")

    