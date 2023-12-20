from sys import stdin

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().split()))
i = 0
j = N - 1
count = 0
    
arr.sort()
    
while i < j:
    if arr[i] + arr[j] < M:
        i += 1
    elif arr[i] + arr[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
    
print(count)
