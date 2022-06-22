N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()
left = 0
right = N-1
ans = 0
while left < N and books[left] < 0:
    ans += abs(books[left])*2
    left += M
while right >= 0 and books[right] > 0:
    ans += books[right]*2
    right -= M
ans -= max(abs(books[0]),abs(books[N-1]))
print(ans)