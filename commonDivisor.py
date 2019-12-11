import math

def euclides_recursivo_mdc(dividendo, divisor):
    if divisor == 0:
        return dividendo
    else:
        return euclides_recursivo_mdc(divisor, dividendo % divisor)



n = int(input())
array = [int(x) for x in input().split()]

if n == 1:
    mdc = array[0]
elif n > 1:
    mdc = euclides_recursivo_mdc(array[0],array[1])
    for i in range(2,n):
        mdc = euclides_recursivo_mdc(mdc, array[i])


count = 0
squarRoot = math.sqrt(mdc)
j = 1
while j<squarRoot:
    if mdc%j == 0:
        count = count + 2
    j += 1

if mdc%squarRoot == 0:
    count += 1
if count == 0:
    count = 1
    
print(count)
