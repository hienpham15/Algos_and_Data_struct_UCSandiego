# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    lut = [None]*(n + 1)
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    
    lut[0] = 0
    lut[1] = 1
    
    for i in range(2, n+1):
        lut[i] = (lut[i-1] + lut[i-2]) % 10
    
    return lut[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))