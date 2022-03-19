inp = input()
op = {}
for x in inp:
    if(x in op):
        op[x] += 1
    else:
        op[x] = 1

if(len(op) % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")