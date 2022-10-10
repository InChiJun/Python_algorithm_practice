from collections import deque
from sys import stdin

n, k = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
q = deque()
ans = []

for i in range(n):
    while q and q[-1][0] > arr[i]:
        q.pop()
    while q and q[0][1] < i - k + 1:
        q.popleft()
    q.append((arr[i], i))
    print(q[0][0], end=' ')