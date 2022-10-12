from sys import stdin

arr = stdin.readline().rstrip()

for i in range(9, -1, -1):
    for j in arr:
        if int(j) == i:
            print(j, end='')