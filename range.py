n = int(input())
array = [int(x) for x in input().split()]
q = int(input())
for k in range(q):
    i, j = [int(x) for x in input().split()]

    min = array[i]
    for i in range(i, j+1):
        if array[i] < min:
            min = array[i]
    print(min)

