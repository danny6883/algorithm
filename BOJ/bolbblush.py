N = int(input())
bin_N = bin(N)
max_xor = '0b' + '1'*(len(bin_N)-2)
small = int(max_xor, 2) - N
if small:
    print('2')
    print(small)
    print(N)
else:
    print('1')
    print(N)