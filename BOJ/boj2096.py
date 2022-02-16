import sys
read = sys.stdin.readline

N = int(read())
score_left_min = 0
score_left_max = 0
score_mid_min = 0
score_mid_max = 0
score_right_min = 0
score_right_max = 0
for _ in range(N):
    left, mid, right = map(int, read().split())
    temp_score_left_min = left + min(score_left_min, score_mid_min)
    temp_score_left_max = left + max(score_left_max, score_mid_max)
    temp_score_mid_min = mid + min(score_left_min, score_mid_min, score_right_min)
    temp_score_mid_max = mid + max(score_left_max, score_mid_max, score_right_max)
    temp_score_right_min = right + min(score_mid_min, score_right_min)
    temp_score_right_max = right + max(score_mid_max, score_right_max)
    
    score_left_min = temp_score_left_min
    score_left_max = temp_score_left_max
    score_mid_min = temp_score_mid_min
    score_mid_max = temp_score_mid_max
    score_right_min = temp_score_right_min
    score_right_max = temp_score_right_max
print(max(score_left_max, score_mid_max, score_right_max), min(score_left_min, score_mid_min, score_right_min))