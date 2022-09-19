from collections import deque

data = "12 3\n1 5 2 3 6 2 3 7 3 5 2 6"

def solution(dataStr):
    dataArr = dataStr.split("\n")
    n = int(dataArr[0].split()[0])
    k = int(dataArr[0].split()[1])

    arr = list(map(int, dataArr[1].split()))
    q = deque()
    ans = []
    for i in range(n):
        while q and q[-1][0] > arr[i]:
            q.pop()
        while q and q[0][1] < i - k + 1:
            q.popleft()
        q.append((arr[i], i))
        print(q[0][0], end = ' ')

solution(data)