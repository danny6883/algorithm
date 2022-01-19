n, m = map(int, input().split())
def count_i(n, m, ii):
    i = ii
    count = 0
    while True:
        count += n // i
        i *= ii
        if i > n:
            break
    i = ii
    while True:
        count -= m // i
        i *= ii
        if i > m:
            break
    m = n - m
    i = ii
    while True:
        count -= m // i
        i *= ii
        if i > m:
            break
    return count
print(min(count_i(n,m,5), count_i(n,m,2)))