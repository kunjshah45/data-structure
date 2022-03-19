inp = input()
if(ord(inp[0])>96):
    op = chr(ord(inp[0])-32) + inp[1:]
else:
    op = inp
print(op)