N = int(input())
ans = 0
for _ in range(N):
    target = input()
    while True:
        temp_AA = target.replace('AA','')
        temp_BB = temp_AA.replace('BB','')
        if len(target) == len(temp_BB):
            break
        target = temp_BB
    if not target:
        ans += 1
print(ans)