#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
d = int(input())
for i0 in range(d):
    x = int(input())

    if x >= 38:
        r = x % 5
        if r >= 3:
            x = x + (5 - r)
    print(x)

