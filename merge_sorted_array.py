def mergeArray(arr1, arr2):
    i,j,k = 0,0,0
    op = [0] * (len(arr1)+len(arr2))
    
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            op[k] = arr1[i]
            i += 1
        else:
            op[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        op[k] = arr1[i]
        i+=1
        k+=1

    while j < len(arr2):
        op[k] = arr2[j]
        j+=1
        k+=1
    return op
    
arr1 = [1,3,5,7,9]
arr2 = [2,4,6,8,10]

op = mergeArray(arr1, arr2)
print(op)