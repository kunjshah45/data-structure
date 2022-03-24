def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    for x in served_orders:
        if(len(take_out_orders) and take_out_orders[0]==x):
            take_out_orders.pop(0)
        elif(len(dine_in_orders) and dine_in_orders[0]==x):
            dine_in_orders.pop(0)
        else:
            return False
    if(len(take_out_orders) != 0 and len(dine_in_orders) != 0):
        return False
    return True

op = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
print(op)