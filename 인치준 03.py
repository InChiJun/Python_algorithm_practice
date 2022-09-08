def sumArray(N, M, inputStr, i, j):
    inputArr = list(map(int, inputStr.split()));
    arr = [0];

    for k in inputArr:
        arr.append(k);

    Sarr = [];
    plus = 0;
    for k in arr: # 합배열 만들기
        plus += k;
        Sarr.append(plus);
    
    print(Sarr[j] - Sarr[i - 1]);

sumArray(5, 3, "5 4 3 2 1", 1, 3);
sumArray(5, 3, "5 4 3 2 1", 2, 4);
sumArray(5, 3, "5 4 3 2 1", 5, 5);