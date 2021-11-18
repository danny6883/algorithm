n, k = map(int, input().split())
num = list(map(int, input()))
result = []
ptr = 0

def erase(ptr):
    if ptr >= len(num):
        result.pop()
        return ptr
    if len(result) == 0 or result[-1] >= num[ptr]:
        result.append(num[ptr])
        ptr += 1
        ptr = erase(ptr)
        return ptr
    if result[-1] < num[ptr]:
        result.pop()
        return ptr
    

for _ in range(k):
    ptr = erase(ptr)

print(''.join(map(str, result)) + ''.join(map(str, num[ptr:])))




# n, k = map(int, input().split())
# num = list(map(int, input()))
# for _ in range(k):
#     for i in range(len(num)):
#         if num[i] < num[i+1]:
#             num.pop(i)
#             break
# print(''.join(map(str, num)))