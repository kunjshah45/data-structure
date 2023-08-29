def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    op = [0] * len(int_list)
    op[0]=1
    for x in range(1, len(int_list)):
        op[x] = op[x-1]*int_list[x-1]
    print(op)

    temp = 1
    for x in range(len(int_list)-1,-1,-1):
        op[x] *= temp
        temp *= int_list[x]

    return op

op = get_products_of_all_ints_except_at_index([1,7,3,4])
print(op)