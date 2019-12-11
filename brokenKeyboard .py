testCase = int(input())

for i in range(testCase):
    string = str(input())
    lenString = len(string)
    working = []
    count = 0
    string = string + '0'
    for i in range(1,lenString+1):
        if string[i-1] == string[i]:
            count += 1
        else:
            if count%2==0:
                if string[i-1] not in working:
                    working.append(string[i-1])
            count = 0
    
    working.sort()
    
    print(''.join(working))