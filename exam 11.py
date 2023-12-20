from inspect import stack
from sys import stdin

N = int(stdin.readline().rstrip())
A = []
for i in range(N):
    A.append(int(stdin.readline().rstrip()))

stack = []
num = 1
result = True
resultList = ""

for i in range(len(A)):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            resultList += "+\n"
        stack.pop()
        resultList += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            resultList += "-\n"
if result:
    print(resultList)