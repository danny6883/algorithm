import sys
read = sys.stdin.readline

N = int(read())
p_head, p_tail = read().rstrip().split('*')
len_p_head = len(p_head)
len_p_tail = len(p_tail)
ans = []
for _ in range(N):
    file = read().rstrip()
    if file[:len_p_head] == p_head and file[-len_p_tail:] == p_tail and len(file) >= len_p_head + len_p_tail:
        ans.append("DA")
    else:
        ans.append("NE")
print('\n'.join(ans))