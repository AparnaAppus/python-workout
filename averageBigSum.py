#!/bin/python3

import os
import sys

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    sum = 0
    for item in ar:
        sum += item
    return sum

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
