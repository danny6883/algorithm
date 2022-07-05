def is_prime(n):
    i = 3
    while i <= n**0.5:
        if n%i == 0:
            return False
        i += 2
    return True

N = int(input())
prime = [2,3,5,7]
for i in range(N-1):
    temp = []
    for p in prime:
        for plus in (1,3,5,7,9):
            if is_prime(p*10+plus):
                temp.append(p*10+plus)
    prime = temp[:]
print('\n'.join(map(str,prime)))