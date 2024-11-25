# 시간초과
import sys

while True:
    a = int(sys.stdin.readline())
    if a == 0:
        break
    count = 0
    for i in range(a+1, 2 * a + 1):
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                count+=1
    print(count)
