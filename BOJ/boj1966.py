import sys, collections
read = sys.stdin.readline

ans = []
for _ in range(int(read())):
    n, m = map(int, read().split())
    document = list(map(int, read().split()))
    document_order = collections.deque([(document[i],i) for i in range(n)])
    count = 0

    find = max(document)
    while True:
        if find == document[m]:
            break
        i = 0
        while i < len(document_order):
            if document_order[i][0] == find:
                document_order.rotate(-i)
                document_order.popleft()
                count += 1
                i = -1
            i += 1
        
        find = 0
        for doc in document_order:
            if doc[0] > find:
                find = doc[0]
    
    for doc in document_order:
        if doc[0] == document[m]:
            count += 1
        if doc[1] == m:
            break

    ans.append(str(count))
print('\n'.join(ans))