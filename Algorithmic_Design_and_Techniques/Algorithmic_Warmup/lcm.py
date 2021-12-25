# python3
import sys


def gcd_euclide(a, b):
    if b == 0:
        return a
    
    new_a = a%b
    return gcd_euclide(b, new_a)


def lcm_naive(a, b):
    result = abs(a*b)//gcd_euclide(a, b)

    return int(result)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))