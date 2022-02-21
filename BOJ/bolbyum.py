N, K = map(int, input().split())
taste = list(map(int, input().split()))
taste += taste[:K-1]
max_taste = sum(taste[:K])
past = max_taste
for i in range(1, N):
    past = past - taste[i-1] + taste[i+K-1]
    if max_taste < past:
        max_taste = past
print(max_taste)