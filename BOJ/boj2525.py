A, B = map(int, input().split())
C = int(input())
B += C
A = (A + B//60)%24
B %= 60
print(A,B)