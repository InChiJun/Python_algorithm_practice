# 백준 시간 초과

from sys import stdin

N, K = map(int, stdin.readline().split())

A = list(map(int, stdin.readline().split()))

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, S, E):
    M = int((S + E) / 2)
    swap(A, S, M)
    pivot = A[S]
    i = S
    j = E
    while i < j:
        while pivot < A[j]:
            j -= 1
        while i < j and pivot >= A[i]:
            i += 1
        swap(A, i, j)
    A[S] = A[i]
    A[i] = pivot
    return i

def qSort(A, S, E, K):
    if S < E:
        pivot = partition(A, S, E)
        if pivot == K:
            return
        elif K < pivot:
            qSort(A, S, pivot - 1, K)
        else:
            qSort(A, pivot + 1, E, K)

qSort(A, 0, N - 1, K - 1)
print(A[K - 1])