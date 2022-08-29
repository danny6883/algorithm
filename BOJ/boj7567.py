arr = input()
ans = 10
for i in range(1,len(arr)):
  if arr[i] == arr[i-1]:
    ans += 5
  else:
    ans += 10
print(ans)
