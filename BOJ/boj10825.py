import sys
read = sys.stdin.readline

N = int(read())
students = [read().split() for _ in range(N)]
students.sort(key=lambda k: k[0])
students.sort(key=lambda k: int(k[3]), reverse=True)
students.sort(key=lambda k: int(k[2]))
students.sort(key=lambda k: int(k[1]), reverse=True)
ans = students[0][0]
for i in range(1,N):
    ans += '\n' + students[i][0]
print(ans)