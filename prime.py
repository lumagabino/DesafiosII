import math

def generatePrimes(n):
    nSqrt = int(math.sqrt(n))
    array = [True for i in range(nSqrt)]

    for i in range(1,nSqrt):
        if array[i] == True:
            j = i**2
            k=0
            while j < n:
                print(j)
                array[j] = False
                k+=1
                j+=k*i

    return array

n = int(input())
primeList = generatePrimes(n)
