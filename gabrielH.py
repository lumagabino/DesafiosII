from collections import Counter

def diff(l1, l2):
    dic1 = Counter(l1)
    dic2 = Counter(l2)

    lista1 = list(dict.fromkeys(l1))
    lista2 = list(dict.fromkeys(l2))

    sum = 0
    for i in lista1:
        if (i in lista2):
            sum += abs(dic1[i]-dic2[i])
            dic1[i] = 0
            dic2[i] = 0
        else:
            sum += dic1[i]

    for i in lista2:
        sum += dic2[i]

    return sum

t = int(input())
for k in range(t):    
    n1, n2 = [int(x) for x in input().split()]
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]    
    

    print(diff(l1, l2))