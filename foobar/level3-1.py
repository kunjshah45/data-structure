# Doomsday Fuel
# =============

# Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

# Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

# Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

# For example, consider the matrix m:
# [
#   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0],  # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
# [0, 3, 2, 9, 14].

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
# Output:
#     [7, 6, 8, 21]

# Input:
# Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
# Output:
#     [0, 3, 2, 9, 14]

# -- Python cases --
# Input:
# solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
# Output:
#     [7, 6, 8, 21]

# Input:
# solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# Output:
#     [0, 3, 2, 9, 14]

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder
# will have to use absorbing markov chain concept here. Refered yt patrickJMT's video to understand the concept.
# identify absorbing state
# identify non adsorbing state
# rearrange the matrix
# divide the matrix depending on number of absording state into 4 parts
# I, 0
# R, Q
# after having R and Q find F. formula for F is (I-Q)^-1. So get I-Q first and use numpy to inverse the thing
# after you have F use F to get P(bar) = I 0
#                                        FR 0
# use FR to get answer
# Simplify the thing to get comman denominator and create a list of numerator and append denominator at the end
from __future__ import division
from fractions import Fraction

def get_absorbing_state(m):
    """
    Function to sum each row equal to 0. and Determine absorbing / Terminal State.
    """
    absorbing_row = []
    for each_row in range(len(m)):
        if sum(m[each_row]) == 0:
            absorbing_row.append(each_row)
    return absorbing_row

def get_rsub_qsub(m, absorbing_rows):
    """
    R sub matrix and Q sub matrix are calulated using absorbing states.
    for each row not in absorbing use to create r and q sub matrix
    as r is in below half meaning in non absorbing state. we check if not in absorbing.
    """
    rsub, qsub = [], []
    for each_row in range(len(m)):
        if each_row not in absorbing_rows:
            # for getting that fraction we use total of row to create probability of that state.
            row_total = sum(m[each_row])
            # we might have multiple non absorbing states. so we making each_rsub and each_qsub.
            each_rsub, each_qsub = [], []
            for each_col in range(len(m[each_row])):
                # this check is done for dividing R and Q. Left side, meaning the absorbing state goes in rsub
                if each_col in absorbing_rows:
                    each_rsub.append(m[each_row][each_col]/row_total)
                else:
                    # this else puts  values to qsub
                    each_qsub.append(m[each_row][each_col]/row_total)
            
            rsub.append(each_rsub)
            qsub.append(each_qsub)
    return rsub, qsub

def identity_matrix(size):
    """
    Function is to create an identity matrix of the given size
    """
    identity = [[int(i == j) for j in range(size)] for i in range(size)]
    return identity

def get_fsub(qsub):
    """
    Function is used to Subtract Q sub matrix and Identity Matrix
    """
    fsub = subtract_matrices(identity_matrix(len(qsub)), qsub)
    return fsub

def get_sub_inverse(m):
    """
    Function is to inverse matrix
    """
    n = len(m)
    identity = identity_matrix(n)
    # Augment the matrix with the identity matrix
    augmented_matrix = [row + identity[i] for i, row in enumerate(m)]
    # Perform row operations
    for i in range(n):
        # Find the pivot row
        pivot_row = i
        while augmented_matrix[pivot_row][i] == 0:
            pivot_row += 1
        # Swap rows to bring the pivot element to the diagonal
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]
        # Scale the pivot row to make the pivot element equal to 1
        pivot = augmented_matrix[i][i]
        for j in range(2 * n):
            augmented_matrix[i][j] /= pivot

        # Perform row operations to make other elements in the column zero
        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(2 * n):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    # Extract the inverted matrix
    inverted_matrix = [row[n:] for row in augmented_matrix]
    return inverted_matrix

def gcd(x, y):
    """
    Function is used to get greatest common divisor
    """
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    """
    Function is used to get LCM of X and Y
    """
    lcmq = (x*y)//gcd(x,y)
    return lcmq
    
def dec_to_frac_with_lcm(l):
    """
    Function is used to convert decimal to fraction and simplify the fraction denominator
    """
    # return arr is the numerator array
    numerators = []
    denominators = []
    for num in l:
        # this loop changes numbers from the list to fractions
        fraction = Fraction(num).limit_denominator()
        # in this two lines we append numerator and denominator into their respective list
        numerators.append(fraction.numerator)
        denominators.append(fraction.denominator)
    # get the lowest common multiple of all the denominators
    lcd = 1
    for denom in denominators:
        lcd = lcm(lcd,denom)
    # after we have the lcm of all the denominators we need to change and multiply numerator to get common denominator
    for num_i in range(len(numerators)):
        numerators[num_i] *= int(lcd/denominators[num_i])
    # as expected in the question we need to append the denominator to the end of the list
    numerators.append(lcd)
    return numerators

def subtract_matrices(m1, m2):
    """
    Function to get subtraction of two given matrix
    """
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] - m2[i][j])
        result.append(row)
    return result

def matrix_multiplication(m1, m2):
    """
    Function to multiply matrix1 and matrix2
    """
    rows1, cols1 = len(m1), len(m1[0])
    rows2, cols2 = len(m2), len(m2[0])

    # the resultant matrix will be numbers of rows of m1 and numbers of cols of m2
    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += m1[i][k] * m2[k][j]

    return result

def solution(m):
    if len(m) < 2:
        return [1, 1]
    # absorbing rows are the states which once entered cannot be exited. Terminating States
    absorbing_rows = get_absorbing_state(m)
    # R sub matrix and Q sub matrix from the matrix
    rsub, qsub = get_rsub_qsub(m=m, absorbing_rows=absorbing_rows)
    # formula for getting F sub matrix. I - Q
    fsub = get_fsub(qsub)
    # after having I-Q inverse the result to get F.
    f = get_sub_inverse(fsub)
    # Multiply the results of F with R sub matrix
    product_FR = matrix_multiplication(f, rsub)
    # the below function is used to convert decimal to fraction and simplify the fraction denominator
    op = dec_to_frac_with_lcm(product_FR[0])
    return op

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
