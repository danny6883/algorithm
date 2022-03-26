scores = [int(input()) for _ in range(10)]
sum_scores = 0
for score in scores:
    if sum_scores + score <= 100:
        sum_scores += score
    else:
        if 100-sum_scores >= sum_scores+score-100:
            sum_scores += score
        break
print(sum_scores)