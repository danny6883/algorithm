N = int(input())
first, second = 1, 1
for i in range((N-1)//2):
    first += second
    second += first
if N%2 == 1:
    print(first)
else:
    print(second)