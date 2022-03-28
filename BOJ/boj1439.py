S = input()
diff = 0
now = S[0]
for alpha in S:
    if now != alpha:
        diff += 1
        now = alpha
print((diff+1)//2)