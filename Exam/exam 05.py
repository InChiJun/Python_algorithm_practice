from sys import stdin


N, M = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
sArr = [arr[0]];
C = []

for i in range(M):
    C.append(0)

for i in range(1, N):
    sArr.append(sArr[i - 1] + arr[i])

remainder = 0
answer = 0
for i in range(N):
    remainder = int(sArr[i] % M);
    if remainder == 0:
        answer += 1
    C[remainder] += 1
    
for i in range(M):
    if C[i] > 1:
        answer = answer + (C[i] * (C[i] - 1) / 2)
print(int(answer))
