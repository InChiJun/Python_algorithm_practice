from sys import stdin
from queue import PriorityQueue

input = stdin.readline

n = int(input().rstrip())
q = PriorityQueue()
for i in range(n):
    q.put(int(input().rstrip()))

# while(not len(q) == 1):
#     q.put(q.get() + q.get())

# print(q.)