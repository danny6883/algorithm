fib = [0,1]
for i in range(20):
    fib.append(fib[i]+fib[i+1])
print(fib[int(input())])