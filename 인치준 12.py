from sys import stdin

n = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().split()))
ans = [0 for i in range(n)]
myStack = []
myStack.append(0)

for i in range(1, n):
    while len(myStack) > 0 and A[myStack[len(myStack) - 1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while len(myStack) > 0:
    ans[myStack.pop()] = -1

for i in range(n):
    print(ans[i], end=" ")