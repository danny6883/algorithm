cnt = 0
for i in range(8):
    row = input()[i%2::2]
    for room in row:
        if room == 'F':
            cnt += 1
print(cnt)