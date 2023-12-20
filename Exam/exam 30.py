from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

sI = max(A)
eI = sum(A)

while sI <= eI:
    mI = int((sI + eI) / 2)
    sum = 0
    count = 0

    for i in range(n):
        if sum + A[i] > mI:
            count += 1
            sum = 0
        
        sum += A[i]
    
    if sum != 0:
        count += 1
    if count > m:
        sI = mI + 1
    else:
        eI = mI - 1
print(sI)