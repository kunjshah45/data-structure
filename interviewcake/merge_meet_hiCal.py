def merge_ranges(meetings):
    meetings = sorted(meetings, key = lambda x:x[0])
    mainOp = [meetings[0]]
    for curr_x,curr_y in meetings[1:]:
        last_x, last_y = mainOp[-1]
        if(curr_x <= last_y):
            mainOp[-1] = (last_x, max(curr_y, last_y))
        else:
            mainOp.append((curr_x, curr_y))
        
    return mainOp


# op = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
op = merge_ranges([(1, 3), (4, 8)])
print(op)
