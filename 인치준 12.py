def solution(dataStr):
    dataArr = dataStr.split("\n")
    n = int(dataArr[0])
    A = list(map(int, dataArr[1].split()))
    ans = [0 for i in range(n)]
    myStack = []
    myStack.append(0)

    for i in range(1, n):
        while len(myStack) > 0 and A[myStack[len(myStack) - 1]] < A[i]:
            ans[myStack.pop()] = A[i]
        myStack.append(i)
    
    while len(myStack) > 0:
        ans[myStack.pop()] = -1
    
    for i in range(n):
        print(ans[i], end=" ")


data1 = "4\n3 5 2 7"
data2 = "4\n9 5 4 8"
solution(data1)
# solution(data2)