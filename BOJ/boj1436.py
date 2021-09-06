n = int(input())
devil = set([666])
jari = 1
while True:
    if n <= len(devil):
        break
    for f_jari in range(jari+1):
        b_jari = jari - f_jari
        if f_jari:
            if b_jari == 0:
                for front in range(10**(f_jari-1), 10**f_jari):
                    devil.add(int(str(front)+str(666)))
            else:
                for front in range(10**(f_jari-1), 10**f_jari):
                    for back in range(10**b_jari):
                        devil.add(int(str(front)+str(666)+str(back).rjust(b_jari,'0')))
        else:
            for back in range(10**b_jari):
                devil.add(int(str(666)+str(back).rjust(b_jari,'0')))
    jari += 1
devil = list(devil)
devil.sort()
print(devil[n-1])