from unittest import result


data = "10\n1 2 3 4 5 6 7 8 9 10"

def solution(datastr):
    dataArr = datastr.split("\n")
    N = int(dataArr[0])
    A = list(map(int, dataArr[1].split()))
    result = 0
    A.sort()

    for k in range(N):
        find = A[k]
        i = 0
        j = N - 1

        while i < j:
            if A[i] + A[j] == find:
                if i != k and j != k:
                    result += 1
                    break
                elif i == k:
                    i += 1
                elif j == k:
                    j -= 1
            elif A[i] + A[j] < find:
                i += 1
            else:
                j -= 1
    
    print(result)


solution(data)