# 출처 : https://www.acmicpc.net/problem/1300

from sys import stdin

input = stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

start = 1
end = k
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(1, n + 1):
        cnt += min(n, (mid // i))
    
    if cnt < k:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)