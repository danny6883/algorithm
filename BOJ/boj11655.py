P = input()
ans = ""
for c in P:
    if ord('A') <= ord(c) <= ord('z'):
        if ord(c)+13>ord("z") or (ord('Z')-13 < ord(c) <= ord('Z')):
            ans += chr(ord(c)-13)
        else:
            ans += chr(ord(c)+13)
    else:
        ans += c
print(ans)