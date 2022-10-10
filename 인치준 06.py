from sys import stdin


# 백준 오답처리
N = int(stdin.readline().rstrip())
count = 1
sI = 1
eI = 1
sum = 1

for i in range(1, N + 1):
    if sum == N:
        eI += 1
        sum += eI
        count += 1
            
    elif sum < N:
        eI += 1
        sum += eI
    else:
        sum -= sI
        sI += 1
    
print(count)