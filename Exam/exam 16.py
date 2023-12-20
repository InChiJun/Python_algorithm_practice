from sys import stdin

N = int(stdin.readline().rstrip())
A = []

for i in range(N):
    A.append((int(stdin.readline().rstrip()), i))

A.sort()
max = 0

for j in range(N):
    index = A[j][1] - j
    if (index > max):
        max = index

print(max + 1)