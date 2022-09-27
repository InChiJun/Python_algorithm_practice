from sys import stdin
import heapq

N = int(stdin.readline())
heap = []

for _ in range(N):
    num = int(stdin.readline())
    if not num == 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)