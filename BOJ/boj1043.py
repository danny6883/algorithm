import sys
read = sys.stdin.readline

N, M = map(int, read().split())
knowTruth = list(map(int, read().split()))
parties = [list(map(int, read().split())) for i in range(M)]

peopleKnowTruth = [0]*(N+1)
for i in range(1,len(knowTruth)):
    peopleKnowTruth[knowTruth[i]] = 1

changed = True
while changed:
    changed = False
    for party in parties:
        if party[0]:
            for i in range(1,len(party)):
                if peopleKnowTruth[party[i]]:
                    party[0] = 0
                    for j in range(1,len(party)):
                        if peopleKnowTruth[party[j]] == 0:
                            peopleKnowTruth[party[j]] = 1
                            changed = True
                    break

cnt = 0
for party in parties:
    if party[0]:
        cnt += 1
print(cnt)