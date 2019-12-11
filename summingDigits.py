n = int(input())
while n != 0:
    sum = 0
    while n > 9:
        sum += n%10
        if sum > 9:
            sum = sum%10 + sum//10
        n = n//10

    sum += n

    if sum > 9:
        sum = sum%10 + sum//10

    print(sum)

    n = int(input())