l = [1,1,1,1,2,3,3,3,3,4,4,4,5,6,7,8,8,8]
n = 1

def sol(l, n):
    return [i for i in l if l.count(i) <= n]

def sol(l, n):
    op = []
    for i in l:
        if l.count(i) <= n:
            op.append(i)
    return op
    

print(sol(l, n))