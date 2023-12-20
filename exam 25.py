from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n

def DFS(v, depth):
    if depth == 4:
        print(1)
        exit()

    for j in graph[v]:
        if not visited[j]:
            visited[j] = True
            DFS(j, depth + 1)
            visited[j] = False


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n):
    visited[i] = True
    DFS(i, 0)
    visited[i] = False

print(0)