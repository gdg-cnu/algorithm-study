a,b = map(int, input().split())

yo = ['SUN','MON','TUE','WED','THU','FRI','SAT']
day = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(a-1):
    b+=day[i]

print(yo[b%7])
