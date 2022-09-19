from itertools import count


data = "6\n9\n2 7 4 1 5 3"

def solution(str):
    dataArr = str.split('\n')
    N = int(dataArr[0])
    M = int(dataArr[1])
    i = 0
    j = N - 1
    count = 0
    
    arr = list(map(int, dataArr[2].split()));
    arr.sort()
    
    while i < j:
        if arr[i] + arr[j] < M:
            i += 1
        elif arr[i] + arr[j] > M:
            j -= 1
        else:
            count += 1
            i += 1
            j -= 1
    
    print(count)


solution(data)