S = input()
ans = ""
stack = []
i = 0
while i < len(S):
    if S[i] == '<':
        ans += ''.join(stack[::-1])
        stack = []
        while S[i] != '>':
            stack.append(S[i])
            i += 1
        stack.append(S[i])
        ans += ''.join(stack)
        stack = []
    elif S[i] == ' ':
        ans += ''.join(stack[::-1])
        ans += ' '
        stack = []
    else:
        stack.append(S[i])
    i += 1
if stack:
    ans += ''.join(stack[::-1])
print(ans)