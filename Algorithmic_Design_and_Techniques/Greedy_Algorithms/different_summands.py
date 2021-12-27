# Uses python3
import sys

def optimal_summands(n):
    summands = []
    rem = n
    prev = 0
    while True:
        cur = prev + 1
        rem -= cur
        if rem <= cur:
            summands.append(rem + cur)
            break
        else:
            prev = cur
            summands.append(cur)
    return summands

ans = optimal_summands(2)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')