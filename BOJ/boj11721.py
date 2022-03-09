N = input()
i = 0
while i < len(N)//10:
    print(N[i*10:(i+1)*10])
    i += 1
print(N[i*10:])