n = int(input())
def hanoi(n, a, b):
    if n == 1:
        global count
        print(a, b)
        return
    else:
        hanoi(n-1, a, 6-a-b)
        hanoi(1, a, b)
        hanoi(n-1, 6-a-b, b)
        return
print(2**n-1)
hanoi(n,1,3)