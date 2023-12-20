from sys import stdin

S, P = map(int, stdin.readline().split())
dna = list(stdin.readline())
tmp = list(map(int, stdin.readline().split()))
check = {'A': tmp[0], 'C': tmp[1], 'G': tmp[2], 'T': tmp[3]}
current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

count = 0
for i in range(S-P+1):
    flag = True

    if i == 0:
        for j in range(P):
            current[dna[j]] += 1
    else:
        current[dna[i+P-1]] += 1
        current[dna[i-1]] -= 1

    for i in ('A', 'C', 'G', 'T'):
        if current[i] < check[i]:
            flag = False
            break

    if flag:
        count += 1

print(count)