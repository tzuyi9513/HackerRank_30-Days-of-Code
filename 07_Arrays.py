#Task
#Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

#Constraints
# 1 <= N <= 1000
# a <= Ai <= 10000 WHERE Ai is the ith integer in the array

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split(' ')))
    a = arr[::-1]

    print(" ".join(str(x) for x in a))
