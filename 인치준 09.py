# 백준 오답 처리

from sys import stdin

S, P = list(map(int, stdin.readline().split()))
DNAArr = stdin.readline().rstrip()
tmp = list(map(int, stdin.readline().split()))
checkArr = {'A': tmp[0], 'C': tmp[1], 'G': tmp[2], 'T': tmp[3]}
myArr = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

cnt = 0

for i in range(S-P+1) :
    for j in range(P) :
        myArr[DNAArr[j+i]] += 1
    success = True
    for j in ['A', 'C', 'G', 'T'] :
        if myArr[j] < checkArr[j] :
            success = False
            break
    if success :
        cnt += 1
    myArr = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

print(cnt)