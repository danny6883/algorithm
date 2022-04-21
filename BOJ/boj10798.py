board = [input() for _ in range(5)]
max_len = len(board[0])
for i in range(1,5):
    if max_len < len(board[i]):
        max_len = len(board[i])
ans = ""
for i in range(max_len):
    for row in range(5):
        if len(board[row]) > i:
            ans += board[row][i]
print(ans)