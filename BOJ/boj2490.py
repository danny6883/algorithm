for _ in range(3):
    turn = input()
    cnt0 = turn.count('0')
    if cnt0:
        print(chr(ord('A')+cnt0-1))
    else:
        print('E')