import math

q = int(input())

for i in range(q): 
    n, m = [int(x) for x in input().split()]
    print(math.gcd( n, m ))