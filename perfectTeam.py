t = int(input())

for i in range(t):
    c, m, x = [int(x) for x in input().split()]
    team = (c+m+x)//3
    result  = min(c, m, team)
    print(result)