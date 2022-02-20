import sys
read = sys.stdin.readline

def preorder(preorder_traversal, node):
    if node != '.':
        preorder_traversal.append(node)
        preorder(preorder_traversal, nodes[node][0])
        preorder(preorder_traversal, nodes[node][1])

def inorder(inorder_traversal, node):
    if node != '.':
        inorder(inorder_traversal, nodes[node][0])
        inorder_traversal.append(node)
        inorder(inorder_traversal, nodes[node][1])

def postorder(postorder_traversal, node):
    if node != '.':
        postorder(postorder_traversal, nodes[node][0])
        postorder(postorder_traversal, nodes[node][1])
        postorder_traversal.append(node)

N = int(read())
nodes = dict()
for i in range(N):
    node, left, right = read().split()
    nodes[node] = (left, right)

preorder_traversal = []
preorder(preorder_traversal, 'A')
inorder_traversal = []
inorder(inorder_traversal, 'A')
postorder_traversal = []
postorder(postorder_traversal, 'A')

print(''.join(preorder_traversal))
print(''.join(inorder_traversal))
print(''.join(postorder_traversal))