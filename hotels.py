n, m = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]

iniIndex=0
soma = 0
maior = 0
for i in range(0, len(values)):
    if soma+values[i]<m:
        soma += values[i]
    elif soma==m:
        break
    else:
        if soma>maior:
            maior=soma
        while soma+values[i]>m:
            soma -= values[iniIndex]
            iniIndex += 1
        soma += values[i]
        if soma>maior:
            maior=soma
    
print(maior)