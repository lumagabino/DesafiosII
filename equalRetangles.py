from collections import Counter 
testCase = int(input())

for i in range(testCase):
    retangles = int(input())
    sides = [int(x) for x in input().split()]
    dic = list(Counter(sides).items())
    dic.sort()
    print(dic)
    
    res = "YES"

    area = dic[0]*dic[-1]
    i = 1
    while dic[i]*dic[-1-i] == area and :
        if dic[i]%2!=0:
            res = "NO"
            break
    print(res)