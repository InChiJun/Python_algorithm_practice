data = "6\n9\n2 7 4 1 5 3"

def solution(str):
    dataArr = str.split('\n')
    N = int(dataArr[0])
    M = int(dataArr[1])
    i = 0
    j = N - 1
    
    arr = list(map(int, dataArr[2].split()));
    arr.sort()
    # arr[]


solution(data)