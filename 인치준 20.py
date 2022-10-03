from sys import stdin

N = int(stdin.readline().rstrip())
A = [0]
for i in range(N):
    A.append(int(stdin.readline().rstrip()))    
tmp = [0 for i in range(N + 1)]

def merget_sort(s, e):
    if e - s < 1:
        return
    m = int(s + (e - s) / 2)

    merget_sort(s, m)
    merget_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = A[i]
    
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= m:
        A[k] = tmp[index2]
        k += 1
        index2 += 1


merget_sort(1, N)
for i in range(1, N + 1):
    print(A[i])