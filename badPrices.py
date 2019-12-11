q = int(input())

for i in range(q): 
    n = int(input())
    array = [int(x) for x in input().split()]

    min = array[-1]
    count = 0

    for i in reversed(array):
        if i <= min:
            min = i
        else:
            count += 1
    
    print(count)