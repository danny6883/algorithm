N, kim, im = map(int, input().split())
round = 0
while kim != im:
    kim = (kim+1)//2
    im = (im+1)//2
    round += 1
print(round)