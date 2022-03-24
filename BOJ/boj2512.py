def bs(left, right):
    if left >= right:
        return left
    elif right - left == 1:
        if sum_budgets - over_budget_cnt*(budgets[over_budget_cnt-1]-right) <= M:
            return right
        else:
            return left
    mid = (left+right)//2
    if sum_budgets - over_budget_cnt*(budgets[over_budget_cnt-1]-mid) <= M:
        return bs(mid, right)
    else:
        return bs(left, mid-1)

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())
sum_budgets = sum(budgets)
ans = 0
if sum_budgets <= M:
    ans = max(budgets)
else:
    budgets.sort(reverse=True)
    over_budget_cnt = 1
    while over_budget_cnt < N:
        if sum_budgets - over_budget_cnt*(budgets[over_budget_cnt-1]-budgets[over_budget_cnt]) <= M:
            ans = bs(budgets[over_budget_cnt],budgets[over_budget_cnt-1])
            break
        else:
            sum_budgets -= over_budget_cnt*(budgets[over_budget_cnt-1]-budgets[over_budget_cnt])
            over_budget_cnt += 1
if ans:
    print(ans)
else:
    print(bs(1,budgets[-1]))