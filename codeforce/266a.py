n = int(input())
inp = input()
count = 0
for x in range(n-1):
    if(inp[x]==inp[x+1]):
        count += 1
print(count)