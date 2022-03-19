inp = list(map(int, input().split("+")))
inp = sorted(inp)
op = ""
for x in inp:
    op = op + str(x) + "+"

op = op[:-1]
print(op)