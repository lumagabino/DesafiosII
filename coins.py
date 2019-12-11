n = int(input())
numbers_with_these_set_bits = [0]*(n+1)
unassigned = 2**n
for i in range(2**n):
    x = i
    set_bits = 0
    
    while x != 0:
        x = x & (x-1)
        set_bits = set_bits+1
    
    numbers_with_these_set_bits[set_bits] = numbers_with_these_set_bits[set_bits]+1
    #print("i = " + str(i))
    #print("set bits:" + str(set_bits))
    
for qtd in range(n+1):
    type = numbers_with_these_set_bits[qtd]
    if type % 2 == 0:
        unassigned = unassigned - type
    else:
        unassigned = unassigned - (type - 1)
        
print(unassigned)