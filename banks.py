from collections import Counter 
import operator

t = int(input())

for i in range(t):
    n = int(input())
    
    accounts = []
    for i in range(n):
        account = input()
        accounts.append(account)

    emptyLine = input()

    dict = Counter(accounts)
    sorted_dict = sorted(dict.items(), 
    key=operator.itemgetter(0))

    for x in sorted_dict:
        print(x[0][:-1], x[1])
