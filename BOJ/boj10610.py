N = input()
sum = 0
zero_to_nine = [0]*10
for num in N:
    zero_to_nine[int(num)] += 1
for i in [1,4,7]:
    sum += zero_to_nine[i]
for i in [2,5,8]:
    sum += 2*zero_to_nine[i]

if zero_to_nine[0]>0 and sum%3 == 0:
    print(''.join([zero_to_nine[i]*str(i) for i in range(9,-1,-1)]))
else:
    print(-1)