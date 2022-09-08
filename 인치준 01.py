def strSum(N, str):
    sum = 0;

    for i in range(N):
        sum += int(str[i]);
    
    print(sum);

strSum(5, "54321");