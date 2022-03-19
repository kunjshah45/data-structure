n = int(input())
count = 0
for x in range(n):
    eachProblem = input().split()
    eachProblem = list(map(int, eachProblem))
    if(sum(eachProblem) >= 2):
        count += 1
print(count)