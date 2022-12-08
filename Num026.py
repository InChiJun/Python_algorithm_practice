"""
문제 026. DFS와 BFS 프로그램 (백준 1260번)

https://www.acmicpc.net/problem/1260
"""
data1 = ['4 5 1', '1 2', '1 3', '1 4', '2 4', '3 4']    # 1 2 4 3\n1 2 3 4
data2 = ['5 5 3', '5 4', '5 2', '1 2', '3 4', '3 1']    # 3 1 2 5 4\n3 1 4 2 5
data3 = ['1000 1 1000', '999 1000'] # 1000 999\n1000 999

def data():
    yield from data1

gen = data()

def readline():
    return next(gen)

from sys import stdin
stdin.readline = readline
# _______________________

# Answer
from collections import deque
from sys import stdin
readline = stdin.readline

def BFS(vertex):
    que = deque()
    que.append(vertex)
    visited[vertex] = 1
    
    while que:
        vertex = que.popleft()
        print(vertex, end = " ")

        for i in range(1, N + 1):
            if visited[i] == 0 and graph[vertex][i] == 1:
                que.append(i)
                visited[i] = 1

def DFS(vertex):
    visited[vertex] = 1
    print(vertex, end = " ")
    for i in range(1, N + 1):
        if visited[i] == 0 and graph[vertex][i] == 1:
            DFS(i)

N, M, V = map(int, readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, readline().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (N + 1)
DFS(V)
print()
visited = [0] * (N + 1)
BFS(V)