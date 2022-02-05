import sys, collections
read = sys.stdin.readline

ans = []
T = int(read())
for _ in range(T):
    A, B = map(int, read().split())
    visited = [[] for i in range(10000)]
    visited[A] = [-1,'']
    DSLR = collections.deque()
    DSLR.append(A)
    while visited[B] == []:
        for i in range(len(DSLR)):
            n = DSLR.popleft()
            D = n*2 % 10000
            S = (n-1) % 10000
            L = n*10%10000 + n*10//10000
            R = n//10 + n%10*1000
            if visited[D] == []:
                DSLR.append(D)
                visited[D] = [n,'D']
                if D == B:
                    break
            if visited[S] == []:
                DSLR.append(S)
                visited[S] = [n,'S']
                if S == B:
                    break
            if visited[L] == []:
                DSLR.append(L)
                visited[L] = [n,'L']
                if L == B:
                    break
            if visited[R] == []:
                DSLR.append(R)
                visited[R] = [n,'R']
                if R == B:
                    break
    temp = ''
    n = B
    while n != -1:
        n, order = visited[n]
        temp = order + temp
    ans.append(temp)
print('\n'.join(ans))