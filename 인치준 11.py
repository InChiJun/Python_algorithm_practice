from inspect import stack


data1 = "8\n4\n3\n6\n8\n7\n5\n2\n1"
data2 = "5\n1\n2\n5\n3\n4"

def solution(dataStr):
    N = int(dataStr.split("\n")[0])
    A = list(map(int, dataStr.split("\n")))
    del A[0]
    stack = []
    num = 1
    result = True
    resultList = ""

    for i in range(len(A)):
        su = A[i]
        if su >= num:
            while su >= num:
                stack.append(num)
                num += 1
                resultList += "+\n"
            stack.pop()
            resultList += "-\n"
        else:
            n = stack.pop()
            if n > su:
                print("NO")
                result = False
                break
            else:
                resultList += "-\n"
    if result:
        print(resultList)


solution(data1)
solution(data2)