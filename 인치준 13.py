import queue

N = int(input())
myQueue = queue.Queue()

for i in range(1, N + 1):
    myQueue.put(i)

while myQueue.qsize() > 1:
    myQueue.get()
    myQueue.put(myQueue.get())

print(myQueue.get())