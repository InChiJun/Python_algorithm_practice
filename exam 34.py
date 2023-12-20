# 출처 : https://www.acmicpc.net/problem/1744

from sys import stdin
input = stdin.readline

N = int(input())
positive  = []
negative = []
max_sum = 0

for _ in range(N):
  n = int(input())
  
  if n > 1:
    positive.append(n)
  elif n == 1:
    max_sum += 1
  else:
    negative.append(n)

positive.sort(reverse=True)
negative.sort()

if len(positive) % 2 == 0:
  for i in range(0, len(positive), 2):
    max_sum += positive[i] * positive[i+1]
else:
  for i in range(0, len(positive)-1, 2): 
    max_sum += positive[i] * positive[i+1]
  max_sum += positive[len(positive)-1]

if len(negative) % 2 == 0:
  for i in range(0, len(negative), 2):
    max_sum += negative[i] * negative[i+1]
else:
  for i in range(0, len(negative)-1, 2):
    max_sum += negative[i] * negative[i+1]
  max_sum += negative[len(negative)-1]

print(max_sum)