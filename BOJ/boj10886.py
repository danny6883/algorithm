import sys
read = sys.stdin.readline

N = int(read())
score = 0
for _ in range(N):
    is_cute = int(read())
    if is_cute:
        score += 1
    else:
        score -= 1
if score > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")