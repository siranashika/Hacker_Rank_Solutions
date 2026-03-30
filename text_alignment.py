n = int(input())
c = 'H'
for i in range(n):
    print((c*(2*i+1)).center(2*n-1))
for i in range(n+1):
    print((c*n).center(2*n) + (c*n).center(6*n))
for i in range((n+1)//2):
    print((c*n*5).center(6*n))
for i in range(n+1):
    print((c*n).center(2*n) + (c*n).center(6*n))
for i in range(n):
    print(((c*(2*(n-i)-1)).center(2*n-1)).rjust(6*n-1))
