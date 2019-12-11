testCase = int(input())
for i in range(testCase):
    objects = int(input())
    minX = 1000 
    minY = 1000 
    maxX = -1000 
    maxY = -1000
    for j in range(objects):
        objs  = [str(z) if z.isalpha() else int(z) for z in input().split()]
        if  objs[0]=='p':
            if objs[1]<minX:
                minX = objs[1]
            if objs[1]>maxX:
                maxX = objs[1]
            if objs[2]<minY:
                minY = objs[2]
            if objs[2]>maxY:
                maxY = objs[2]
        elif  objs[0]=='l':
            if objs[1]<minX:
                minX = objs[1]
            if objs[1]>maxX:
                maxX = objs[1]
            if objs[2]<minY:
                minY = objs[2]
            if objs[2]>maxY:
                maxY = objs[2]
            if objs[3]<minX:
                minX = objs[3]
            if objs[3]>maxX:
                maxX = objs[3]
            if objs[4]<minY:
                minY = objs[4]
            if objs[4]>maxY:
                maxY = objs[4]
        elif objs[0]=='c':
            leftButtonX = objs[1]-objs[3]
            leftButtonY = objs[2]-objs[3]
            rightTopX = objs[1]+objs[3]
            rightTopY = objs[2]+objs[3]
            if leftButtonX<minX:
                minX = leftButtonX
            if leftButtonY<minY:
                minY = leftButtonY
            if rightTopX>maxX:
                maxX = rightTopX
            if rightTopY>maxY:
                maxY = rightTopY
    print(minX, minY, maxX, maxY)  
    emptyLine = str(input())
    