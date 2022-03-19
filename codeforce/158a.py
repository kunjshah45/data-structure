n,thres = input().split()
thres = int(thres)
count = 0
listOfData = list(map(int, input().split()))
for x in listOfData:
    if(x >= listOfData[thres-1] and x>0):
        count += 1
print(count)