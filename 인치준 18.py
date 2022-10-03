from sys import stdin

N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().split(' ')))
S = [0 for i in range(N)]

for i in range(1, N):
    insertIndex = i
    insertValue = A[i]
    
    for j in range(i - 1, -1, -1):
        if A[j] < A[i]:
            insertIndex = j + 1
            break

        if j == 0:
            insertIndex = 0

    for j in range(i, insertIndex, -1):
        A[j] = A[j - 1]

    A[insertIndex] = insertValue

S[0] = A[0]
for i in range(1, N):
    S[i] = A[i] + S[i - 1]

sum = 0
for i in range(N):
    sum += S[i]

print(sum)





# 5
# 3 1 4 3 2