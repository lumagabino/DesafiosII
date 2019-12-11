t = int(input())
for i in range(t):
    n = int(input())
    
    sum=0
    i=5
    while i<=n:
        sum += n//i
        i*=5
    print(sum)

