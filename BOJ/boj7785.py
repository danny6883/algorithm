n = int(input())
in_comp = dict()
for _ in range(n):
    name, log = input().split()
    if log == "enter":
        in_comp[name] = 1
    else:
        in_comp.pop(name)
ans = list(in_comp.keys())
ans.sort(reverse = True)
print('\n'.join(ans))