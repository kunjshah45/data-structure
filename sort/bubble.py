def bubble(arr):
    for x in range(0, len(arr)):
        for y in range(0, len(arr)):
            if(arr[x] < arr[y]):
                arr[x], arr[y] = arr[y], arr[x]
    return arr

arr = [8,7,6,5,4,3,2,1]
op = bubble(arr)
print("op: ", op)