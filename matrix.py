from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    arrA = []
    arrB = []
    for j in range(n):
        a, b = [int(z) for z in input().split()]
        arrA.append(a)
        arrB.append(b)
        
    dictA = Counter(arrA)
    dictB = Counter(arrB)

    print(dictA)
    print(dictB)

    for j in range(n):
        
