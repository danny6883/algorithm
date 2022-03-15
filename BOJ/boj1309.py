N = int(input())
first, second = 1, 3
for _ in range(N//2):
    first = (first+second*2)%9901
    second = (first*2+second)%9901
if N%2:
    print(second)
else:
    print(first)