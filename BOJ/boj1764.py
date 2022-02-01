import sys
read = sys.stdin.readline

N, M = map(int, read().split())
no_listen = dict()
for _ in range(N):
    no_listen[read().rstrip()] = 1
no_listen_and_see = []
for _ in range(M):
    no_see = read().rstrip()
    if no_see in no_listen:
        no_listen_and_see.append(no_see)
print(len(no_listen_and_see))
print('\n'.join(sorted(no_listen_and_see)))