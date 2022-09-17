from collections import deque

from pyparsing import empty

data = "12 3\n1 5 2 3 6 2 3 7 3 5 2 6"

def solution(dataStr):
    dataArr = dataStr.split("\n")
    N = dataArr[0].split()[0]
    L = dataArr[0].split()[1]
    mydeque = deque(map(int, dataArr[1].split()))
    numbersList = dataArr[1].split()
    
    for i in numbersList:
        while (not mydeque.empty & mydeque.)


solution(data)