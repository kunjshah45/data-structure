def selection(arr):
    for x in range(0, len(arr)):
        curmin = x
        for y in range(x+1, len(arr)):
            if(arr[y] < arr[curmin]):
                curmin = y
            if(x!=curmin):
                arr[x], arr[curmin] = arr[curmin], arr[x]        
    return arr

arr = [20,12,10,15,2]
op = selection(arr)
print(op)