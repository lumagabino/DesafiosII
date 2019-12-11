from collections import Counter

t = int(input())
for i in range(t): 
    arrX = [int]
    arrY = [int]
    
    n = int(input())
    for j in range(n):      
        x, y = [int(x) for x in input().split()]
        arrX.append(x)
        arrY.append(y)

    dicX = Counter(arrX)
    dicY = Counter(arrY)

    arrayX = list(dict.fromkeys(arrX))
    arrayY = list(dict.fromkeys(arrY))

    arrayX.pop(0)
    arrayY.pop(0)

    prod = 0
    first = True
    for i in arrayX:
        if i in arrayY:
            prod += (dicX[i] * dicY[i])
    print(prod)