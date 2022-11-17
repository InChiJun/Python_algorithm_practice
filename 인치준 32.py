# 출처 : https://www.acmicpc.net/problem/11047

from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
cnt = 0
A = []
for i in range(n):
    A.append(int(input().rstrip()))

for i in range(len(A) - 1, -1, -1):
    if (k // A[i]) > 0:
        cnt += k // A[i]
        k %= A[i]

print(cnt)