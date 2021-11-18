n = int(input())

col = [True] * n
dia1 = [True] * (2*n-1)
dia2 = [True] * (2*n-1)
ans = 0

def queen(num):
    global ans
    if num == n:
        ans += 1
        return
    for i in range(n):
        if col[i] and dia1[num+i] and dia2[n-1+num-i]:
            col[i] = False
            dia1[num+i] = False
            dia2[n-1+num-i] = False
            
            queen(num+1)
            
            col[i] = True
            dia1[num+i] = True
            dia2[n-1+num-i] = True
queen(0)
print(ans)