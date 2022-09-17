data = "9 8\nCCTGGATTG\n2 0 1 1"
def solution(dataStr):
    def add(c):
        if c == 'A':
            myArr[0] += 1
            if (myArr[0] == checkArr[0]):
                checkSecret += 1

        if c == 'C':
            myArr[1] += 1
            if (myArr[1] == checkArr[1]):
                checkSecret += 1

        if c == 'G':
            myArr[2] += 1
            if (myArr[2] == checkArr[2]):
                checkSecret += 1

        if c == 'T':
            myArr[3] += 1
            if (myArr[3] == checkArr[3]):
                checkSecret += 1


    def remove(c):
        if c == 'A':
            if (myArr[0] == checkArr[0]):
                checkSecret -= 1
            myArr[0] -= 1

        if c == 'C':
            if (myArr[1] == checkArr[1]):
                checkSecret -= 1
            myArr[1] -= 1

        if c == 'G':
            if (myArr[2] == checkArr[2]):
                checkSecret -= 1
            myArr[2] -= 1

        if c == 'T':
            if (myArr[3] == checkArr[3]):
                checkSecret -= 1
            myArr[3] -= 1

    dataArr = dataStr.split('\n')
    firstLine = dataArr[0].split()
    S = int(firstLine[0]) # 문자열 크기
    P = int(firstLine[1]) # 부분 문자열 크기
    str = dataArr[1] # DNA 문자열
    checkArr = dataArr[2].split() # 조건
    checkSecret = 0 # 조건 맞는지 체크하는 변수
    myArr = [0, 0, 0, 0]
    result = 0

    for i in checkArr:
        if i == 0:
            checkSecret += 1
    
    for i in range(P):
        add(str[i])
    
    if checkSecret == 4:
        result += 1
    
    # for i in 
    
    


solution(data)