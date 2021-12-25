# python3

def calc_fib(n):
    lut = [None]*(n+1)
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    
    lut[0] = 0
    lut[1] = 1
    
    for i in range(2, n+1):
        lut[i] = lut[i-1] + lut[i-2]
    
    return lut[n]

n = int(input())
print(calc_fib(n))