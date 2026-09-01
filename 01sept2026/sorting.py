#!/bin/python3

import math
import os
import random
import re
import sys

def countSwaps(a):
    # Write your code here
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    print('fructose and sucrose')
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
