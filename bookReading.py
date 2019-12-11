q = int(input())

for i in range(q): 
    n, m = [int(x) for x in input().split()]

    numberOfTimes = (n//m)//10
    count = 0

    sum = 0
    for i in range(1,11,1):
        sum += (m*i)%10
    
    count = sum * numberOfTimes
    
    rest = (n//m)%10
    for j in range(1,rest+1,1):
        count += (m*j)%10

    print(count)