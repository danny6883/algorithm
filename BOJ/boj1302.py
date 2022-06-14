import sys
read = sys.stdin.readline

N = int(read())
books = dict()
for _ in range(N):
    book = read().rstrip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1
max_cnt = 0
ans = ''
for book in books:
    if books[book] > max_cnt:
        max_cnt = books[book]
        ans = book
    elif books[book] == max_cnt and ans > book:
        ans = book
print(ans)