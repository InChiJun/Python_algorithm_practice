N = 5;
M = 3;
arr = [0, 5, 4, 3, 2, 1];
Sarr = [0, 5];

for k in range (2, 6):
    Sarr.append(Sarr[k - 1] + arr[k]);

i = 1;
j = 3;

print(Sarr[j] - Sarr[i - 1]);