g = int(input())
girls = [int(x) for x in input().split()]
b = int(input())
boys = [int(x) for x in input().split()]

girls.sort()
boys.sort()


count = 0
j = 0
i = 0
while i < g and j < b:
    if abs(girls[i]-boys[j]) <= 1:
         count += 1
         j += 1
         i += 1
    elif girls[i]<boys[j]:
        i += 1
    else:
        j += 1

print(count)

