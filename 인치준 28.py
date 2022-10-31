from sys import stdin
from collections import deque

input = stdin.readline
V = int(input().rstrip())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

def bfs(start):
    visit = [-1] * (V + 1)
    dq = deque()
    dq.append(start)
    visit[start] = 0
    max = [0, 0]

    while dq:
        t = dq.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                dq.append(e)
                if max[0] < visit[e]:
                    max = visit[e], e

    return max

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)