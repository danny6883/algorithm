N = int(input())
test_areas = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = N
for test_area in test_areas:
    test_area -= B
    if test_area > 0:
        cnt += test_area // C
        if test_area % C:
            cnt += 1
print(cnt)