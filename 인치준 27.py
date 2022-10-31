from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 상하좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def bfs(x, y):
    
    dq = deque()
    dq.append((x,y))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1: # 범위 검사와 가능경로 검사
                dq.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1     # 한 칸씩 전진할 때마다 +1 해준다.
    
    return graph[n-1][m-1]

print(bfs(0,0))