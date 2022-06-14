input_str = input()
bomb = input()
last_bomb = bomb[-1]
len_bomb = len(bomb)
stack = []
ans = []
for character in input_str:
    stack.append(character)
    if character == last_bomb:
        if stack[-len_bomb:] == list(bomb):
            for _ in range(len_bomb):
                stack.pop()
        else:
            ans += stack
            stack = []
ans += stack
if ans:
    print(''.join(ans))
else:
    print("FRULA")