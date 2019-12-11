n = int(input())
array = [int(x) for x in input().split()]

oddSum = 0
pairSum = 0

for elem in array:
    if elem % 2 == 0:
        pairSum += 1
    else:
        oddSum += 1

if pairSum > oddSum:
    print(oddSum)
else:
    print(pairSum)