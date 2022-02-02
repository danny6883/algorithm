import sys
read = sys.stdin.readline

func = [1,2,4,7,13,24,44,81,149,274,504]

ans = []
for _ in range(int(read())):
    ans.append(str(func[int(read())-1]))
print('\n'.join(ans))