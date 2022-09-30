from sys import stdin

A = list(map(int, stdin.readline().rstrip()))
max = [(0, 0)]

for i in range(len(A)):
    for j in range(i, len(A)):
        if A[j] > max[0][0]:
            max[0] = (A[j], j)
    temp = A[0]
    A[0] = max[0][0]
    A[max[0][1]] = temp
    max = [(0, 0)]

for i in range(len(A)):
    print(A[i], end='')