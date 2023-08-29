"""
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time. 

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good! 

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. 
Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. 
Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. 
For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution('2', '1')
Output:
    1

Input:
Solution.solution('4', '7')
Output:
    4

-- Python cases --
Input:
solution.solution('4', '7')
Output:
    4

Input:
solution.solution('2', '1')
Output:
    1
"""
def solution(x, y):
    # convert str to int
    mach = int(x)
    facula = int(y)
    # var count stores number of operations
    count = 0
    # this while condition runs if Mach and Facula are not same and greater then 0
    while mach != facula and mach > 0 and facula > 0:
        if mach > facula:
            # this if checks for mach value being high 10x Facula
            if mach > 10 * facula:
                # calculate how many iteration would it take if facula is s
                multi = (int(mach//facula) - 1)
                # add multi as it stores how many times I will have to subtract Facula from mach
                count += multi
                # after adding it to gen subtract number 3
                mach = mach - (multi*facula)
            else:
                mach = mach - facula
                count += 1
        else:
            # the same process for facula and mach where facula is greater
            if facula > 10 * mach:
                multi = (int(facula//mach) -1)
                count += multi
                facula = facula - (multi*mach)
            else:
                facula = facula - mach
                count += 1
        
    if mach == 1 and facula == 1:
        return str(count)
    else:
        return "impossible"


print(solution('4', '7'))
print(solution('2', '1'))
print(solution('2', '4'))
print(solution('10000', '1'))