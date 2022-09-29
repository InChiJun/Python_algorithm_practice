from sys import stdin

N = int(stdin.readline().rstrip())
A = []

for i in range(N):
    A.append(int(stdin.readline().rstrip()))

for i in range(N):
    for j in range(N - i):
        if j < 4:
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp

for i in A:
    print(i)