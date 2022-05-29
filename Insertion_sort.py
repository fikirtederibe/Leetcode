[200~#!/bin/python3

        import math
        import os
        import random
        import re
        import sys

        #
        # Complete the 'insertionSort1' function below.
        #
        # The function accepts following parameters:
        #  1. INTEGER n
        #  2. INTEGER_ARRAY arr
        #

        n = int(input())
        d = [int(x) for x in input().split()]
        t = d[n-1]
        k = n-2
        while k >= 0 and t < d[k]:
            d[k+1] = d[k]
                f = str(d)[1:-1].replace(",", "")
                    print(f)
                        k -= 1
                        d[k+1] = t
                        f = str(d)[1:-1].replace(",", "")
                        print(f)
                                                






