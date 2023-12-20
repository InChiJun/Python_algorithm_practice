from sys import stdin
input = stdin.readline

N = int(input())

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if int(num) % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(10):
            temp = number * 10 + i
            if isPrime(temp) == True:
                DFS(temp)

DFS(2)
DFS(3)
DFS(5)
DFS(7)