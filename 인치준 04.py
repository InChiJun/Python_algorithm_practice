def prefixSum(N, M, str0, str1, str2, str3, ask):
    arr = [];
    for i in range(N):
        arr.append(str(i))    


prefixSum(4, 3, "1 2 3 4", "2 3 4 5", "3 4 5 6", "4 5 6 7", "2 2 3 4");
prefixSum(4, 3, "1 2 3 4", "2 3 4 5", "3 4 5 6", "4 5 6 7", "3 4 3 4");
prefixSum(4, 3, "1 2 3 4", "2 3 4 5", "3 4 5 6", "4 5 6 7", "1 1 4 4");