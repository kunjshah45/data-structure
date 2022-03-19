x,y = input().split()
x,y = int(x), int(y)
area = x*y
domi = 0
if(area%2 == 0):
    domi = area/2
else:
    domi = (area-1)/2
print(int(domi))