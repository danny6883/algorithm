identifier = input()
Cpp = False
Java = False
if '_' in identifier:
    Cpp = True
for c in identifier:
    if c.isupper():
        Java = True
        break
ans = ""
if (len(identifier)>0 and (identifier[0].isupper() or identifier[0]=='_')) or (Cpp and Java):
    ans = "Error!"
else:
    if Cpp:
        i = 0
        while i < len(identifier):
            if identifier[i] == '_':
                if i+1 >= len(identifier) or identifier[i+1] == '_':
                    ans = "Error!"
                    break
                ans += identifier[i+1].upper()
                i += 2
            else:
                ans += identifier[i]
                i += 1
    elif Java:
        for c in identifier:
            if c.isupper():
                ans += '_'+c.lower()
            else:
                ans += c
    else:
        ans = identifier
print(ans)