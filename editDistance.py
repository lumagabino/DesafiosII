def checkAlternating(string):
    count = 0
    upper = True
    for i in string:
        if i.isupper() == upper:
            count += 1
        upper = not upper

    result = min((len(string)-count), count)
    print(result)


while True:
    try:
        s = str(input())
        checkAlternating(s)
    except EOFError:
        break
