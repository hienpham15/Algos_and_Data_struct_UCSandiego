# Uses python3
import sys

def gcd_euclide(a, b):
    
    if b == 0:
        return a
    
    new_a = a%b
    return gcd_euclide(b, new_a)

#ans = gcd_euclide(3918848, 1653264)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclide(a, b))