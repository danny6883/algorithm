n, m = map(int, input().split())
out = []
def dfs():
    if len(out) == m:
        print(' '.join(map(str, out)))
        return
    for i in range(1, n+1):
        out.append(i)
        dfs()
        out.pop()
dfs()