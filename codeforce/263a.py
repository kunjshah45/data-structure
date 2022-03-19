inp = []
for x in range(5):
    inp.append(list(map(int, input().split())))
row, col = 0,0
for x in range(5):
    find = False
    for y in range(5):
        val = inp[x][y]
        if(val == 1):
            row, col = x, y
            find = True
            break
    if find:
        break

print(abs(2-row)+abs(2-col))