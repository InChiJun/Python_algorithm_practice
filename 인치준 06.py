from sys import stdin

N = int(stdin.readline().rstrip())
count = 1
start_index = 1
end_index = 1
sum = 1

while(end_index != N):
    if(sum == N):
        count += 1
        end_index += 1
        sum += end_index
    elif(sum > N):
        sum -= start_index
        start_index += 1
    elif(sum < N):
        end_index += 1
        sum = sum + end_index

print(count)