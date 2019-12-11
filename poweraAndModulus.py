def pot(a,b,meio):
    n=1
    for _ in range(b):
        n=meio*n
        n=n%a
    return n


a, b = [int(x) for x in input().split()]

if a%2 == 0:
    print(pot(a,b,a//2))
else:
    print(0)