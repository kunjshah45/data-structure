str1 = input().lower()
str2 = input().lower()
op = 0
str1Val, str2Val = 0, 0

for x in range(len(str1)):
    print(ord(str1[x]), ord(str2[x]))
    str1Val += ord(str1[x])
    str2Val += ord(str2[x])

print(str1Val, str2Val)
if(str1Val > str2Val):
    op = 1
elif(str2Val > str1Val):
    op = -1
else:
    op = 0
print(op)