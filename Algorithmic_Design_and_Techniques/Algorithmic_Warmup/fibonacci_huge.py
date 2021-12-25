# Uses python3
import sys


def get_pisano_length(modulo):
    previous = 1
    current = 1
 
    result = 1
    while not (previous == 0 and current == 1):  # 1
        buffer = (previous + current) % modulo  # 2
        previous = current
        current = buffer
 
        result += 1
 
    return result


def calc_fib(n):
    lut = [None]*(n + 1)
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    
    lut[0] = 0
    lut[1] = 1
    
    for i in range(2, n+1):
        lut[i] = lut[i-1] + lut[i-2]
    
    return lut[n]


def get_fibonacci_huge(n, m):
    
    if n < 2:
        return n
    
    p_length = get_pisano_length(m)
   
    rem = n%p_length
    ans = calc_fib(rem)%m

    return ans

#a = get_fibonacci_huge(2816213588, 239)


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))