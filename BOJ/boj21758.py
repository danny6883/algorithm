N = int(input())
honey = list(map(int, input().split()))
sum_honey = sum(honey)
ans = sum_honey - honey[0] - honey[N-1] + max(honey[1:N-1])

right = sum_honey - honey[0] - 2*honey[1]
max_right = right
for i in range(2,N-1):
    right += honey[i-1]
    right -= 2*honey[i]
    max_right = max(max_right, right)
ans = max(ans, sum_honey - honey[0] + max_right)

left = sum_honey - honey[N-1] - 2*honey[N-2]
max_left = left
for i in range(N-3,0,-1):
    left += honey[i+1]
    left -= 2*honey[i]
    max_left = max(max_left, left)
ans = max(ans, sum_honey - honey[N-1] + max_left)

print(ans)