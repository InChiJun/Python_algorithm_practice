from sys import stdin

N = int(stdin.readline().rstrip())
str = list(stdin.readline().rstrip())
sum = 0

for i in range(N):
    sum += int(str[i])
    
print(sum)