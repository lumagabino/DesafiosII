from collections import Counter  

testCase = int(input())

for t in range(testCase):
    n, m = [int(x) for x in input().split()]

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    dicA = Counter(a)
    dicB = Counter(b)

    a = list(dict.fromkeys(a))
    b = list(dict.fromkeys(b))

    for i in dicA: 
        if (i in dicB):
            if dicA[i] > dicB[i]:
                dicA[i] = dicA[i]-dicB[i]
                dicB[i] = 0
            else:
                dicB[i] = dicB[i]-dicA[i]
                dicA[i] = 0

    sum = 0
    for j in dicA:
        sum = sum + dicA[j]
    for k in dicB:
        sum = sum + dicB[k]
    
    print(sum)