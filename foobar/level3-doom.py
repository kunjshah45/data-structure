from __future__ import division
from fractions import Fraction

def solution(m):
    if len(m) < 2:
        return [1, 1]
    absorbing_rows = get_absorbing_state(m)
    rsub, qsub = get_rsub_qsub(m=m, absorbing_rows=absorbing_rows)
    fsub = get_fsub(qsub)
    f = get_sub_inverse(fsub)
    product_FR = matrix_multiplication(f, rsub)
    op = dec_to_frac_with_lcm(product_FR[0])
    return op
    
def get_absorbing_state(m):
    absorbing_row = []
    for each_row in xrange(len(m)):
        if sum(m[each_row]) == 0:
            absorbing_row.append(each_row)
    return absorbing_row

def get_rsub_qsub(m, absorbing_rows):
    rsub, qsub = [], []
    for each_row in xrange(len(m)):
        if each_row not in absorbing_rows:
            row_total = sum(m[each_row])
            each_rsub, each_qsub = [], []
            for each_col in xrange(len(m[each_row])):
                if each_col in absorbing_rows:
                    each_rsub.append(m[each_row][each_col]/row_total)
                else:
                    each_qsub.append(m[each_row][each_col]/row_total)
            
            rsub.append(each_rsub)
            qsub.append(each_qsub)
    return rsub, qsub

def identity_matrix(size):
    identity = [[int(i == j) for j in xrange(size)] for i in xrange(size)]
    return identity

def get_fsub(qsub):
    fsub = subtract_matrices(identity_matrix(len(qsub)), qsub)
    return fsub

def get_sub_inverse(m):
    n = len(m)
    identity = identity_matrix(n)
    augmented_matrix = [row + identity[i] for i, row in enumerate(m)]
    for i in xrange(n):
        pivot_row = i
        while augmented_matrix[pivot_row][i] == 0:
            pivot_row += 1
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]
        pivot = augmented_matrix[i][i]
        for j in xrange(2 * n):
            augmented_matrix[i][j] /= pivot

        for k in xrange(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in xrange(2 * n):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    inverted_matrix = [row[n:] for row in augmented_matrix]
    return inverted_matrix

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    lcmq = (x*y)//gcd(x,y)
    return lcmq
    
def dec_to_frac_with_lcm(l):
    numerators = []
    denominators = []
    for num in l:
        fraction = Fraction(num).limit_denominator()
        numerators.append(fraction.numerator)
        denominators.append(fraction.denominator)
    lcd = 1
    for denom in denominators:
        lcd = lcm(lcd,denom)
    for num_i in xrange(len(numerators)):
        numerators[num_i] *= int(lcd/denominators[num_i])
    numerators.append(lcd)
    return numerators

def subtract_matrices(m1, m2):
    result = []
    for i in xrange(len(m1)):
        row = []
        for j in xrange(len(m1[i])):
            row.append(m1[i][j] - m2[i][j])
        result.append(row)
    return result

def matrix_multiplication(m1, m2):
    rows1, cols1 = len(m1), len(m1[0])
    rows2, cols2 = len(m2), len(m2[0])
    result = [[0] * cols2 for _ in xrange(rows1)]
    for i in xrange(rows1):
        for j in xrange(cols2):
            for k in xrange(cols1):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

testcase1 = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
]
testcase2 = [
    [0, 2, 1, 0, 0], 
    [0, 0, 0, 3, 4], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]
]
print(solution(m=testcase1))
print(solution(m=testcase2))