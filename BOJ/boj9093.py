import sys
read = sys.stdin.readline

T = int(read())
for _ in range(T):
    sent = read().rstrip().split()
    rev_sent = ''
    for word in sent:
        rev_sent += word[::-1] + ' '
    print(rev_sent.rstrip())