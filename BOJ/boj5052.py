import sys
read = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search_end(self, string):
        curr_node = self.head
        for i in range(len(string)):
            if string[i] in curr_node.children:
                curr_node = curr_node.children[string[i]]
            elif i > 0 and curr_node.children == {}:
                return True
            else:
                return False
        return True

t = int(read())
ans = []
for _ in range(t):
    trie = Trie()
    n = int(read())
    temp_ans = "YES"
    for i in range(n):
        tel = read().rstrip()
        if trie.search_end(tel):
            temp_ans = "NO"
            for j in range(n-i-1):
                read()
            break
        trie.insert(tel)
    ans.append(temp_ans)
print('\n'.join(ans))