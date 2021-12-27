# python3

import sys
import math

def IsGreaterOrEqual(digit, maxDigit):
    if maxDigit == -math.inf:
        return True
    a = str(digit) + str(maxDigit)
    b = str(maxDigit) + str(digit)
    
    if int(a) >= int(b):
        return True
    else:
        return False


def largest_number(a):
    ans = ''
    while a:
        maxDigit = -math.inf
        for digit in a:
            if IsGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        
        ans += str(maxDigit)
        a.remove(maxDigit)
    return ans


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))