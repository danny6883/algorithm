import sys
read = sys.stdin.readline

people = list()
for _ in range(int(read())):
    age, name = map(str, read().split())
    people.append((int(age), name))
people.sort(key = lambda k: k[0])
for person in people:
    print(' '.join(map(str,person)))