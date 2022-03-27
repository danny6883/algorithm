import sys
read = sys.stdin.readline

N = int(read())
words = dict()
for _ in range(N):
    words[read().rstrip()] = 1
for word in words:
    if word[::-1] in words:
        print(len(word), word[len(word)//2])
        break