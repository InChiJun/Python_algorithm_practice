N, M = map(int, input().split()); # N, M 할당
arr = [0];
arr = list(map(int, input().split())); # arr 배열 받기

Sarr = [];
plus = 0;
for i in arr: # 합배열 만들기
    plus += i;
    Sarr.append(plus);

for k in range(M):
    i, j = map(int, input().split());
    print(Sarr[j + 1] - Sarr[i - 1]);