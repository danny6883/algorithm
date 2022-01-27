L = int(input())
STR = input()
mod = 1234567891
hash = 0
for i in range(L):
    hash += (ord(STR[i]) - ord('a') + 1) * (31**i) % mod
hash %= mod
print(hash)