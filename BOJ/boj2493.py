N = int(input())
tower_height = list(map(int, input().split()))
stack = [(tower_height[0],1)]
laser_receive = [0]

for i in range(1,N):
    flag = False
    while stack:
        height, index = stack.pop()
        if height >= tower_height[i]:
            laser_receive.append(index)
            if height > tower_height[i]:
                stack.append((height,index))
            stack.append((tower_height[i],i+1))
            flag = True
            break
    if not flag:
        laser_receive.append(0)
        stack = [(tower_height[i],i+1)]
print(*laser_receive)