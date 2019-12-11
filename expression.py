def trasform(exp):
    operator = []
    variable = []
    result = []

    for i in exp:
        if i == ')':
            result += variable
            variable = []
            result += operator.pop()
        elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
            operator.append(i)
        elif i != '(':
            variable.append(i)

    result = ''.join(result)
    print(result)



n = int(input())

for i in range(n): 
    e = str(input())
    trasform(e)
