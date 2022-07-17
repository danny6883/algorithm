N = int(input())
ingre = [list(map(int, input().split())) for _ in range(N)]
ingre.sort()
ans = 1000000000
for bi in range(1,2**N):
    temp = [1,0]
    for i in range(N):
        if bi % 2:
            temp[0] *= ingre[i][0]
            temp[1] += ingre[i][1]
            if temp[0] - temp[1] >= ans:
                break
        bi //= 2
    ans = min(ans, abs(temp[0]-temp[1]))
print(ans)