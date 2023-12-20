from sys import stdin

N = int(stdin.readline().rstrip())
M = []

for i in range(N):
    M.append(int(stdin.readline().rstrip()))

for i in range(len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i], M[j] = M[j], M[i]

for n in M:
    print(n)