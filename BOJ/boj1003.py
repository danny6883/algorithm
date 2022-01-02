ns = []
for _ in range(int(input())):
    ns.append(int(input()))
fib0 = [1,0]
fib1 = [0,1]
for i in range(2,41):
    fib0.append(fib0[i-2] + fib0[i-1])
    fib1.append(fib1[i-2] + fib1[i-1])
for n in ns:
    print(fib0[n], fib1[n])