expr = input()
cases = set()

stack = []
paren_pair = []
for i in range(len(expr)):
    if expr[i] == '(':
        stack.append(i)
    elif expr[i] == ')':
        left = stack.pop()
        paren_pair.append([left,i])

paren_cases = [[]]
for pair in paren_pair:
    temp = []
    for case in paren_cases:
        temp.append(case[:])
    for i in range(len(temp)):
        temp[i] += pair
    paren_cases += temp
paren_cases.pop(0)
for i in range(len(paren_cases)):
    paren_cases[i].sort()

for paren_case in paren_cases:
    temp = list(expr)
    for index in paren_case[::-1]:
        temp.pop(index)
    cases.add(''.join(temp))

cases = list(cases)
cases.sort()
print('\n'.join(cases))