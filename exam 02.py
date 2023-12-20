from sys import stdin

N = int(stdin.readline().rstrip())
scoreArr = list(map(int, stdin.readline().split()))

sum = 0
max = 0

for i in scoreArr:
    sum += i
    if max < i:
        max = i
    
print(sum * 100.0 / max / N)
