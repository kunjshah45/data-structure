n = int(input())
count = 0
for x in range(n):
    operation = input()
    if(operation[1]=="+"):
        count += 1
    else:
        count -= 1
print(count)