import sys
sys.setrecursionlimit(10**6)

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = postorder[post_end]
    ans.append(root)
    preorder(in_start, index[root]-1, post_start, post_start+index[root]-in_start-1)
    preorder(index[root]+1, in_end, post_end+index[root]-in_end, post_end-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
index = [0]*(n+1)
for i in range(n):
    index[inorder[i]] = i
ans = []
preorder(0, n-1, 0, n-1)
print(*ans)