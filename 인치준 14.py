from sys import stdin
import heapq

N = int(stdin.readline().rstrip())
heap = []

for i in range(N):
    num = int(stdin.readline().rstrip())
    if not num == 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)