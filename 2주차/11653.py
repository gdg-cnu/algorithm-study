# 소인수분해
num = int(input())
i = 2                    #나눌 수를 2로 지정
while num > 1:           
    if num % i == 0:
        num = num // i
        print(i)
    else:
        i += 1
