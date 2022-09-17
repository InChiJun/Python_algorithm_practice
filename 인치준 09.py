data = '9 8\nCCTGGATTG\n2 0 1 1'
data2 = '4 2\nGATA\n1 0 0 1'

def Solution(data) :
    data = data.split('\n')
    first = list(map(int, data[0].split(' ')))
    S, P = first[0], first[1]
    DNAArr = data[1]
    tmp = list(map(int, data[2].split(' ')))
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

    return print(cnt)

Solution(data)
Solution(data2)