
def hanoi(n, fr, to, temp):
	if n==1:
		print(fr, to)
		return 1
	else:
		hanoi(n-1,fr,temp,to) #마지막 원판 제외 보조기둥으로 이동
		print(fr, to) # 가장 큰 원판 이동
		hanoi(n-1,temp,to,fr) # 마지막 원판 제외 보조에서 대상기둥으로 이동

n=int(input())
print(2**n-1)
if n<=20:
    hanoi(n,1,3,2)
