MOD = 1000000
code = input()
case = [0]*(len(code)+1)
case[0] = 1
case[1] = 1
for i in range(1,len(code)):
  if code[i] == '0':
    if not(code[i-1] == '1' or code[i-1] == '2'):
      break
  if 10 <= 10*int(code[i-1]) + int(code[i]) <= 26:
    if 10*int(code[i-1]) + int(code[i]) == 10 or 10*int(code[i-1]) + int(code[i]) == 20:
      case[i+1] += case[i-1] % MOD
    else:
      case[i+1] += (case[i-1] + case[i]) % MOD
  else:
    case[i+1] += case[i] % MOD
if int(code) == 0 or code[0] == '0':
  print(0)
else:
  print(case[-1])
