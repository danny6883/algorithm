N = int(input())
cases = [987654312]*(N+1)
cases[1] = 1

i = 2
while True:
    if i**2 > N:
        break
    cases[i**2] = 1
    i += 1

for num in range(2,N+1):
    i = 1
    while True:
        if i**2 > num or cases[num] <= 2:
            break
        cases[num] = min(cases[num], cases[i**2] + cases[num - i**2])
        i += 1

print(cases[N])