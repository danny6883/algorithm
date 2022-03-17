import sys
read = sys.stdin.readline

N, M  = map(int, read().split())
min_pack, min_one = map(int, read().split())
for _ in range(M-1):
    pack, one = map(int, read().split())
    if min_pack > pack:
        min_pack = pack
    if min_one > one:
        min_one = one
min_money = min_one*N
if min_money > min_pack*(N//6) + min_one*(N%6):
    min_money = min_pack*(N//6) + min_one*(N%6)
if min_money > min_pack*(N//6+1):
    min_money = min_pack*(N//6+1)
print(min_money)