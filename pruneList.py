def CountFrequency(my_list): 
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq
    # for key, value in freq.items(): 
    #     print ("% d : % d"%(key, value)) 
  


if __name__ == "__main__":  
    testCase = input()

    while(testCase>0):
        n, m = raw_input().split(" ")

        a = []
        a = map(int, raw_input().split(" "))
        a.sort()

        b = []
        b = map(int, raw_input().split(" "))
        b.sort()

        # for x in range(len(a)): 
        #     print a[x]
        # for x in range(len(b)): 
        #     print b[x]
        
        a = CountFrequency(a)
        b = CountFrequency(b) 

        for keyA, freqA in a.items(): 
            for keyB, freqB in b.items():
                if keyA == keyB:
                    if freqA > freqB:
                        a[keyA] = freqA-freqB
                        b[keyB] = 0
                    else:
                        b[keyB] = freqB-freqA
                        a[keyA] = 0
        
        # for key, value in a.items(): 
        #     print ("% d : % d"%(key, value))
        # print("------------") 
        # for key, value in b.items(): 
        #     print ("% d : % d"%(key, value))

        sum = 0
        for keyA, freqA in a.items():
            sum = sum + freqA
        for keyB, freqB in b.items():
            sum = sum + freqB
        print(sum)

        testCase = testCase - 1
