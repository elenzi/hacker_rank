#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    count = 1
    while count < 11:
        result = count*n
        print(n, "x", count, "=", result)
        count += 1
