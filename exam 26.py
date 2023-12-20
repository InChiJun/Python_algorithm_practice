from collections import deque
from sys import stdin

input = stdin.readline
    
def dfs(v):
    visited_dfs[v] = True
    order_dfs.append(v)
    for i in node[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    visited_bfs[v] = True
    order_bfs.append(v)
    queue = deque([v])
    while queue:
        x = queue.popleft()
        for i in node[x]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                order_bfs.append(i)
                queue.append(i)

n, m, start = map(int, input().split())
node = []
for _ in range(n+1):
    node.append([])

for _ in range(m):
    x, y = map(int, input().split())
    node[x].append(y)
    node[x].sort()
    node[y].append(x)
    node[y].sort()

visited_dfs = [False] * (n+1)
order_dfs = []
visited_bfs = [False] * (n+1)
order_bfs = []

dfs(start)
print(*order_dfs)
bfs(start)
print(*order_bfs)