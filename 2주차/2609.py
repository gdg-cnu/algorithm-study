#2609번-최대공약수와 최소공배수
#유클리드호
m,n = map(int,input().split())
gcf=0 #최대공약수
def gcd(m,n):
    if m<n:
        m,n = n,m
    if n==0:
        return m
    if m%n ==0:
        return n
    else:
        return gcd(n,m%n)
gcf=gcd(m,n)
lcm=gcf*(m//gcf)*(n//gcf)
print(gcf)
print(lcm)