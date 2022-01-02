from itertools import combinations
import sys

n = int(sys.stdin.readline().strip())
s = []
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().strip().split())))
min = 987654321
teams = list(combinations(list(range(n)),n//2))
for team in teams:
    start = team[:]
    link = list(set(list(range(n)))-set(start))
    temp = 0
    for first in start:
        for second in start:
            temp += s[first][second]
    for first in link:
        for second in link:
            temp -= s[first][second]
    if temp < 0:
        temp *= -1
    if min > temp:
        min = temp
print(min)