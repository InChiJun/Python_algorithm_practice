from sys import stdin

N, M = list(map(int, stdin.readline().split()))
inputArr = list(map(int, stdin.readline().split()))
arr = [0]

for k in inputArr:
    arr.append(k)

Sarr = []
plus = 0
for k in arr: # 합배열 만들기
    plus += k
    Sarr.append(plus)

for k in range(M):
    i, j = list(map(int, stdin.readline().split()))
    print(Sarr[j] - Sarr[i - 1])
