def averageScore(N, scoreStr):
    scoreArr = list(map(int, scoreStr.split()));
    sum = 0;
    max = 0;

    for i in scoreArr:
        sum += i;
        if max < i:
            max = i;
    
    print(sum * 100.0 / max / N);

averageScore(3, "40 80 60");