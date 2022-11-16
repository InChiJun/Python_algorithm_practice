from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
count = 0

def merge(left, right):
    global count
    i, j = 0, 0
    temp = []
    while i < len(left) and j < len(right):

        if left[i] > right[j]:
            temp.append(right[j])
            j += 1
            count += len(left) - i

        else:
            temp.append(left[i])
            i += 1

    if i == len(left):
        temp.extend(right[j:])
    else:
        temp.extend(left[i:])
    return temp


def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        mid = len(list) // 2
        left = merge_sort(list[: mid])
        right = merge_sort(list[mid:])
        return merge(left, right)


A = merge_sort(A)
print(count)